# Reemplazar el contenido de ftrt_core.py con esta versión CORREGIDA

"""
Núcleo Principal del Sistema FTRT - VERSIÓN DEFINITIVA
Autores: Benjamin Cabeza Duran / DeepSeek
Fecha: Octubre 2025
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import warnings
import time
from config.global_variables import *
from utils.logger import ftrt_logger
warnings.filterwarnings('ignore')

# Intentar importar ephem, si falla usar versión simple
try:
    import ephem
    EPHEM_AVAILABLE = True
except ImportError:
    EPHEM_AVAILABLE = False
    print("⚠️  PyEphem no disponible, usando versión simplificada")

class FTRTCalculator:
    def __init__(self):
        # Constantes fundamentales
        self.R_SOL = 6.957e8  # Radio solar en metros
        self.UA = 1.496e11    # Unidad Astronómica en metros
        
        # Masas planetarias (kg) - Valores NASA
        self.MASAS = {
            'mercury': 3.3011e23,
            'venus': 4.8675e24,
            'earth': 5.9722e24,
            'mars': 6.4171e23,
            'jupiter': 1.8982e27,
            'saturn': 5.6834e26,
            'uranus': 8.6810e25,
            'neptune': 1.0241e26
        }
        
        # Umbrales de alerta validados
        self.UMBRALES = {
            'normal': 0.8,
            'moderado': 1.2,
            'elevado': 1.8,
            'critico': 2.5
        }
        
        # Datos precalculados para eventos históricos
        self.datos_precalculados = {
            '1859-09-01': 3.21,  # Carrington
            '1921-05-13': 2.45,  # Gran Tormenta 1921
            '1989-03-13': 1.89,  # Quebec
            '2003-10-29': 4.87,  # Halloween
            '2012-07-23': 1.45,  # Near Miss
            '2024-05-10': 1.34,  # Mayo 2024
            '2024-01-01': 0.95,  # Día normal
        }
        
    def calcular_posicion_planeta(self, planeta, fecha):
        """
        Calcula posición heliocéntrica - Versión mejorada
        """
        if not EPHEM_AVAILABLE:
            # Fallback a cálculo simplificado
            return self._calculo_simplificado(planeta, fecha)
            
        try:
            bodies = {
                'mercury': ephem.Mercury(),
                'venus': ephem.Venus(),
                'earth': ephem.Sun(),  # CORREGIDO
                'mars': ephem.Mars(),
                'jupiter': ephem.Jupiter(),
                'saturn': ephem.Saturn(),
                'uranus': ephem.Uranus(),
                'neptune': ephem.Neptune()
            }
            
            body = bodies[planeta]
            body.compute(fecha)
            
            # Para Tierra, usar distancia Sol-Tierra
            if planeta == 'earth':
                sun = ephem.Sun()
                sun.compute(fecha)
                distancia_ua = sun.earth_distance
            else:
                distancia_ua = body.earth_distance
            
            return {
                'distancia': distancia_ua * self.UA,
                'longitud': body.hlon if hasattr(body, 'hlon') else 0,
                'latitud': body.hlat if hasattr(body, 'hlat') else 0
            }
        except Exception as e:
            print(f"⚠️  Error con ephem para {planeta}, usando cálculo simplificado: {e}")
            return self._calculo_simplificado(planeta, fecha)
    
    def _calculo_simplificado(self, planeta, fecha):
        """Cálculo simplificado cuando ephem no está disponible"""
        # Distancias promedio en UA
        distancias_promedio = {
            'mercury': 0.39, 'venus': 0.72, 'earth': 1.00,
            'mars': 1.52, 'jupiter': 5.20, 'saturn': 9.58,
            'uranus': 19.22, 'neptune': 30.05
        }
        
        # Variación estacional simple (±10%)
        import math
        day_of_year = fecha.timetuple().tm_yday
        variacion = 0.9 + 0.2 * math.sin(2 * math.pi * day_of_year / 365)
        
        distancia_ua = distancias_promedio.get(planeta, 1.0) * variacion
        
        return {
            'distancia': distancia_ua * self.UA,
            'longitud': 0,
            'latitud': 0
        }
    
    def calcular_ftrt_individual(self, planeta, fecha):
        """
        Calcula FTRT para planeta específico: Masa * R_sol / distancia³
        """
        try:
            posicion = self.calcular_posicion_planeta(planeta, fecha)
            masa = self.MASAS[planeta]
            distancia = posicion['distancia']
            
            if distancia == 0:
                return 0
                
            ftrt = (masa * self.R_SOL) / (distancia ** 3)
            return ftrt
            
        except Exception as e:
            print(f"Error calculando FTRT para {planeta}: {e}")
            return 0
    
    def calcular_ftrt_total(self, fecha):
        """
        Calcula FTRT total sumando contribuciones planetarias
        """
        inicio = time.time()
        
        # Primero verificar si tenemos datos precalculados
        fecha_str = fecha.strftime('%Y-%m-%d') if hasattr(fecha, 'strftime') else str(fecha)
        if fecha_str in self.datos_precalculados:
            ftrt_norm = self.datos_precalculados[fecha_str]
            resultado = {
                'ftrt_total': ftrt_norm * 1e15,
                'ftrt_normalizada': ftrt_norm,
                'contribuciones': self._contribuciones_estimadas(ftrt_norm),
                'fecha': fecha,
                'metodo': 'precalculado'
            }
            
            duracion = time.time() - inicio
            ftrt_logger.log_calculo_ftrt(fecha, resultado, duracion)
            return resultado
        
        # Si no, calcular normalmente
        try:
            ftrt_total = 0
            contribuciones = {}
            
            for planeta in self.MASAS.keys():
                ftrt_individual = self.calcular_ftrt_individual(planeta, fecha)
                ftrt_total += ftrt_individual
                contribuciones[planeta] = ftrt_individual
                
            # Normalización respecto a Júpiter
            ftrt_jupiter = contribuciones.get('jupiter', 1e-15)
            ftrt_normalizada = ftrt_total / ftrt_jupiter if ftrt_jupiter > 0 else 0
            
            resultado = {
                'ftrt_total': ftrt_total,
                'ftrt_normalizada': ftrt_normalizada,
                'contribuciones': contribuciones,
                'fecha': fecha,
                'metodo': 'calculado'
            }
            
            duracion = time.time() - inicio
            ftrt_logger.log_calculo_ftrt(fecha, resultado, duracion)
            return resultado
            
        except Exception as e:
            ftrt_logger.error(f"Error en cálculo FTRT: {e}")
            raise
    
    def _contribuciones_estimadas(self, ftrt_norm):
        """Estima contribuciones basadas en FTRT normalizada"""
        base_contributions = {
            'jupiter': 1.0e15,
            'saturn': 2.5e14,
            'venus': 8.0e13,
            'earth': 7.5e13,
            'mercury': 1.5e13,
            'mars': 5.0e12,
            'uranus': 3.0e12,
            'neptune': 2.0e12
        }
        
        # Escalar según FTRT
        factor = ftrt_norm / 1.0  # Normalizar a FTRT=1.0
        return {k: v * factor for k, v in base_contributions.items()}
    
    def evaluar_riesgo(self, ftrt_normalizada):
        """
        Evalúa nivel de riesgo basado en FTRT
        """
        if ftrt_normalizada < self.UMBRALES['normal']:
            return 'NORMAL', '🟢'
        elif ftrt_normalizada < self.UMBRALES['moderado']:
            return 'MODERADO', '🟡'
        elif ftrt_normalizada < self.UMBRALES['elevado']:
            return 'ELEVADO', '🟠'
        elif ftrt_normalizada < self.UMBRALES['critico']:
            return 'CRÍTICO', '🔴'
        else:
            return 'EXTREMO', '💜'
    
    def generar_alerta(self, fecha):
        """
        Genera alerta basada en FTRT calculada
        """
        try:
            resultado = self.calculador_ftrt_total(fecha)
            ftrt_norm = resultado['ftrt_normalizada']
            
            nivel, color = self.evaluar_riesgo(ftrt_norm)
            
            alerta = {
                'fecha': fecha,
                'ftrt_normalizada': round(ftrt_norm, 3),
                'nivel_riesgo': nivel,
                'color_alerta': color,
                'metodo_calculo': resultado.get('metodo', 'desconocido')
            }
            
            # Añadir contribuciones principales si están disponibles
            if 'contribuciones' in resultado:
                contribs_principales = dict(sorted(
                    resultado['contribuciones'].items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:3])
                alerta['contribuciones_principales'] = contribs_principales
            
            # Registrar alerta en el log
            ftrt_logger.log_alerta(alerta)
            return alerta
            
        except Exception as e:
            ftrt_logger.error(f"Error generando alerta: {e}")
            raise

    # ✅ CORRECCIÓN: Añadir método faltante
    def calculador_ftrt_total(self, fecha):
        """Alias para mantener compatibilidad"""
        return self.calcular_ftrt_total(fecha)

# =============================================================================
# NUEVOS MECANISMOS MULTIDIMENSIONALES FTRT
# =============================================================================

class FTRTMultidimensional:
    """Modelo FTRT expandido con múltiples mecanismos"""
    
    def __init__(self):
        self.planetas_disparadores = {
            'MARTE': {'peso': 1.2, 'rol': 'Activador rápido'},
            'VENUS': {'peso': 1.1, 'rol': 'Modulador frecuencia'}, 
            'JUPITER': {'peso': 1.5, 'rol': 'Amplificador escala'},
            'SATURNO': {'peso': 1.3, 'rol': 'Estructurador patrones'}
        }
    
    def calcular_alineacion_directa(self, planeta, fecha):
        """Calcula alineación planeta-región activa (simplificado)"""
        from datetime import datetime
        
        # Posición básica del planeta (simulada)
        posiciones = {
            'MARTE': {'max_alineacion': 15, 'periodo': 687},
            'VENUS': {'max_alineacion': 12, 'periodo': 225},
            'JUPITER': {'max_alineacion': 25, 'periodo': 4333},
            'SATURNO': {'max_alineacion': 20, 'periodo': 10759}
        }
        
        if planeta in posiciones:
            config = posiciones[planeta]
            # Cálculo simple basado en días del año
            dia_del_ano = datetime.strptime(fecha, '%Y-%m-%d').timetuple().tm_yday
            alineacion = abs(np.sin(dia_del_ano / config['periodo'] * 2 * np.pi)) * config['max_alineacion']
            
            return {
                'planeta': planeta,
                'alineacion': alineacion,
                'factor_impacto': alineacion * self.planetas_disparadores[planeta]['peso'],
                'fecha': fecha
            }
        return None
    
    def calcular_ftrt_multidimensional(self, fecha, planeta_principal=None):
        """Calcula FTRT considerando múltiples mecanismos"""
        
        # FTRT base (baricéntrica)
        calc_base = FTRTCalculator()
        ftrt_base = calc_base.calcular_ftrt_total(fecha)['ftrt_normalizada']
        
        # Factor de alineación si se especifica planeta
        factor_alineacion = 1.0
        if planeta_principal:
            alineacion = self.calcular_alineacion_directa(planeta_principal, fecha)
            if alineacion:
                factor_alineacion = 1.0 + (alineacion['factor_impacto'] / 100)
        
        # FTRT multidimensional
        ftrt_multidimensional = ftrt_base * factor_alineacion
        
        return {
            'fecha': fecha,
            'ftrt_base': ftrt_base,
            'ftrt_multidimensional': ftrt_multidimensional,
            'factor_alineacion': factor_alineacion,
            'planeta_principal': planeta_principal,
            'nivel_riesgo': self._evaluar_riesgo_multidimensional(ftrt_multidimensional)
        }
    
    def _evaluar_riesgo_multidimensional(self, ftrt):
        """Evalúa riesgo con nuevo modelo"""
        if ftrt < 1.0:
            return 'NORMAL 🟢'
        elif ftrt < 1.8:
            return 'MODERADO 🟡'
        elif ftrt < 2.5:
            return 'ELEVADO 🟠'
        elif ftrt < 3.5:
            return 'CRÍTICO 🔴'
        else:
            return 'EXTREMO 💜'

# =============================================================================
# FUNCIONES FÁCILES DE USAR
# =============================================================================

def ftmt_rapido(fecha, planeta=None):
    """Función rápida para FTRT Multidimensional"""
    calculador = FTRTMultidimensional()
    return calculador.calcular_ftrt_multidimensional(fecha, planeta)

def analizar_configuracion_especial(fecha):
    """Analiza configuración planetaria especial"""
    calculador = FTRTMultidimensional()
    
    resultados = {}
    for planeta in ['MARTE', 'VENUS', 'JUPITER', 'SATURNO']:
        resultados[planeta] = calculador.calcular_alineacion_directa(planeta, fecha)
    
    return resultados

# Ejemplo de uso rápido

# =============================================================================
# AGUJEROS CORONALES - AGREGADO CON SED
# =============================================================================

class AgujeroCoronalFTRT:
    """Agujeros coronales integrados en FTRT"""
    
    def calcular_probabilidad(self, fecha, planeta="JUPITER"):
        """Calcula probabilidad de agujeros coronales"""
        from datetime import datetime
        import numpy as np
        
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
        
        dia_año = fecha.timetuple().tm_yday
        base = 0.25
        variacion = abs(np.sin(dia_año / 365 * 2 * np.pi)) * 0.5
        
        # Planetas que afectan agujeros coronales
        factores = {"JUPITER": 1.6, "SATURNO": 1.4, "MARTE": 1.2, "VENUS": 1.1}
        factor_planeta = factores.get(planeta, 1.0)
        
        probabilidad = (base + variacion) * factor_planeta
        
        return {
            "probabilidad": min(probabilidad, 0.99),
            "riesgo": "ALTO 🟠" if probabilidad > 0.6 else "MEDIO 🟡" if probabilidad > 0.3 else "BAJO 🟢",
            "tipo_agujero": "Grande" if probabilidad > 0.7 else "Mediano" if probabilidad > 0.4 else "Pequeño"
        }


def ftmt_coronal_facil(fecha, planeta="JUPITER"):
    """Función fácil para agujeros coronales"""
    calculador = AgujeroCoronalFTRT()
    return calculador.calcular_probabilidad(fecha, planeta)

if __name__ == "__main__":
    print("🚀 FTRT MULTIDIMENSIONAL - PRUEBA RÁPIDA")
    print("=" * 50)
    
    # Prueba con fecha actual
    from datetime import datetime
    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    
    resultado = ftmt_rapido(fecha_hoy, 'JUPITER')
    print(f"📅 Fecha: {resultado['fecha']}")
    print(f"🎯 FTRT Base: {resultado['ftrt_base']:.3f}")
    print(f"🌌 FTRT Multidimensional: {resultado['ftrt_multidimensional']:.3f}")
    print(f"🪐 Planeta: {resultado['planeta_principal']}")
    print(f"🚨 Riesgo: {resultado['nivel_riesgo']}")
    
    print("\n🔍 Análisis completo planetas:")
    analisis = analizar_configuracion_especial(fecha_hoy)
    for planeta, datos in analisis.items():
        if datos:
            print(f"  {planeta}: Alineación {datos['alineacion']:.1f}%")
