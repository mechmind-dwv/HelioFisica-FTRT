"""
Sistema de Logging FTRT
Autor: Benjamin Cabeza Duran / DeepSeek
Fecha: Octubre 2025

Este módulo implementa un sistema de logging avanzado para el proyecto FTRT,
permitiendo el seguimiento detallado de cálculos, predicciones y eventos.
"""

import logging
import sys
from datetime import datetime
import os
import json
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

class FTRTLogger:
    """Logger especializado para el sistema FTRT"""
    
    NIVELES = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    
    def __init__(self, nombre="FTRT", nivel="INFO"):
        """
        Inicializa el logger con configuración específica para FTRT
        
        Args:
            nombre (str): Nombre del logger
            nivel (str): Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self.logger = logging.getLogger(nombre)
        self.logger.setLevel(self.NIVELES.get(nivel, logging.INFO))
        self.nombre = nombre
        
        # Crear directorio de logs si no existe
        self.log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Configurar handlers
        self._configurar_handlers()
        
        self.logger.info(f"🌟 Logger FTRT inicializado - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def _configurar_handlers(self):
        """Configura los handlers para diferentes tipos de logs"""
        # Limpiar handlers existentes
        self.logger.handlers = []
        
        # 1. Handler para consola con formato colorido
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self._ColorFormatter())
        self.logger.addHandler(console_handler)
        
        # 2. Handler para archivo general con rotación por tamaño
        file_handler = RotatingFileHandler(
            os.path.join(self.log_dir, 'ftrt.log'),
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setFormatter(self._crear_formato_archivo())
        self.logger.addHandler(file_handler)
        
        # 3. Handler para eventos críticos con rotación diaria
        eventos_handler = TimedRotatingFileHandler(
            os.path.join(self.log_dir, 'eventos_criticos.log'),
            when='midnight',
            interval=1,
            backupCount=30
        )
        eventos_handler.setLevel(logging.WARNING)
        eventos_handler.setFormatter(self._crear_formato_archivo())
        self.logger.addHandler(eventos_handler)
        
        # 4. Handler para métricas en JSON
        self.metricas_file = os.path.join(self.log_dir, 'metricas.json')
    
    def _crear_formato_archivo(self):
        """Crea el formato para los archivos de log"""
        return logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    class _ColorFormatter(logging.Formatter):
        """Formateador con colores para la consola"""
        COLORES = {
            'DEBUG': '\033[94m',     # Azul
            'INFO': '\033[92m',      # Verde
            'WARNING': '\033[93m',   # Amarillo
            'ERROR': '\033[91m',     # Rojo
            'CRITICAL': '\033[95m',  # Magenta
            'RESET': '\033[0m'
        }
        
        def format(self, record):
            color = self.COLORES.get(record.levelname, self.COLORES['RESET'])
            record.msg = f"{color}{record.msg}{self.COLORES['RESET']}"
            return record.msg
    
    def log_calculo_ftrt(self, fecha, resultado, duracion=None):
        """
        Registra un cálculo FTRT
        
        Args:
            fecha (datetime): Fecha del cálculo
            resultado (dict): Resultado del cálculo FTRT
            duracion (float): Duración del cálculo en segundos
        """
        msg = f"📊 Cálculo FTRT - {fecha.strftime('%Y-%m-%d')}"
        msg += f" | FTRT: {resultado['ftrt_normalizada']:.3f}"
        if duracion:
            msg += f" | ⏱️ {duracion:.3f}s"
            
        nivel = self._determinar_nivel_log(resultado['ftrt_normalizada'])
        getattr(self.logger, nivel.lower())(msg)
        
        # Guardar métricas
        self._guardar_metrica('calculo', {
            'fecha': fecha.isoformat(),
            'ftrt': resultado['ftrt_normalizada'],
            'duracion': duracion,
            'timestamp': datetime.now().isoformat()
        })
    
    def log_prediccion(self, fecha_prediccion, ftrt_predicha, confianza):
        """
        Registra una predicción FTRT
        
        Args:
            fecha_prediccion (datetime): Fecha para la que se predice
            ftrt_predicha (float): Valor FTRT predicho
            confianza (float): Nivel de confianza de la predicción
        """
        msg = f"🔮 Predicción - {fecha_prediccion.strftime('%Y-%m-%d')}"
        msg += f" | FTRT: {ftrt_predicha:.3f} | Confianza: {confianza:.2%}"
        
        nivel = self._determinar_nivel_log(ftrt_predicha)
        getattr(self.logger, nivel.lower())(msg)
        
        self._guardar_metrica('prediccion', {
            'fecha_prediccion': fecha_prediccion.isoformat(),
            'ftrt': ftrt_predicha,
            'confianza': confianza,
            'timestamp': datetime.now().isoformat()
        })
    
    def log_alerta(self, alerta):
        """
        Registra una alerta del sistema
        
        Args:
            alerta (dict): Información de la alerta
        """
        msg = f"⚠️ {alerta['nivel_riesgo']} {alerta['color_alerta']}"
        msg += f" | FTRT: {alerta['ftrt_normalizada']:.3f}"
        
        nivel = self._nivel_alerta_a_log(alerta['nivel_riesgo'])
        getattr(self.logger, nivel.lower())(msg)
        
        if nivel in ['WARNING', 'ERROR', 'CRITICAL']:
            self._guardar_metrica('alerta', {
                'nivel': alerta['nivel_riesgo'],
                'ftrt': alerta['ftrt_normalizada'],
                'timestamp': datetime.now().isoformat()
            })
    
    def _determinar_nivel_log(self, ftrt):
        """Determina el nivel de log basado en FTRT"""
        if ftrt < 0.8:
            return 'INFO'
        elif ftrt < 1.2:
            return 'INFO'
        elif ftrt < 1.8:
            return 'WARNING'
        elif ftrt < 2.5:
            return 'ERROR'
        else:
            return 'CRITICAL'
    
    def _nivel_alerta_a_log(self, nivel_alerta):
        """Convierte nivel de alerta a nivel de log"""
        mapping = {
            'NORMAL': 'INFO',
            'MODERADO': 'INFO',
            'ELEVADO': 'WARNING',
            'CRÍTICO': 'ERROR',
            'EXTREMO': 'CRITICAL'
        }
        return mapping.get(nivel_alerta, 'WARNING')
    
    def _guardar_metrica(self, tipo, datos):
        """Guarda métrica en archivo JSON"""
        try:
            if os.path.exists(self.metricas_file):
                with open(self.metricas_file, 'r') as f:
                    metricas = json.load(f)
            else:
                metricas = {'calculos': [], 'predicciones': [], 'alertas': []}
            
            if tipo == 'calculo':
                metricas['calculos'].append(datos)
            elif tipo == 'prediccion':
                metricas['predicciones'].append(datos)
            elif tipo == 'alerta':
                metricas['alertas'].append(datos)
            
            with open(self.metricas_file, 'w') as f:
                json.dump(metricas, f, indent=2)
                
        except Exception as e:
            self.logger.error(f"Error guardando métrica: {e}")
    
    def debug(self, msg): self.logger.debug(msg)
    def info(self, msg): self.logger.info(msg)
    def warning(self, msg): self.logger.warning(msg)
    def error(self, msg): self.logger.error(msg)
    def critical(self, msg): self.logger.critical(msg)

# Crear instancia global del logger
ftrt_logger = FTRTLogger()

if __name__ == "__main__":
    # Ejemplo de uso
    logger = FTRTLogger(nivel="DEBUG")
    
    # Log de diferentes niveles
    logger.debug("🔍 Debugging FTRT")
    logger.info("ℹ️ Sistema funcionando normalmente")
    logger.warning("⚠️ FTRT elevado detectado")
    logger.error("❌ Error en cálculo")
    logger.critical("🚨 ¡Evento crítico inminente!")
    
    # Log de cálculo FTRT
    from datetime import datetime
    logger.log_calculo_ftrt(
        datetime.now(),
        {'ftrt_normalizada': 2.1},
        duracion=0.45
    )
    
    # Log de predicción
    logger.log_prediccion(
        datetime.now(),
        ftrt_predicha=1.8,
        confianza=0.95
    )
    
    # Log de alerta
    logger.log_alerta({
        'nivel_riesgo': 'CRÍTICO',
        'color_alerta': '🔴',
        'ftrt_normalizada': 2.1
    })
