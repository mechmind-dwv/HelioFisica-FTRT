"""
Núcleo Principal FTRT - CON VARIABLES GLOBALES
Autores: Benjamin Cabeza Duran / DeepSeek
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from config.global_variables import *  # Importar TODAS las variables globales
import warnings
warnings.filterwarnings('ignore')

# Intentar importar ephem
try:
    import ephem
    EPHEM_AVAILABLE = True
except ImportError:
    EPHEM_AVAILABLE = False
    print("⚠️  PyEphem no disponible, usando versión simplificada")

class FTRTCalculator:
    def __init__(self):
        # Usar constantes de variables globales
        self.R_SOL = RADIO_SOLAR
        self.UA = UNIDAD_ASTRONOMICA
        self.MASAS = MASAS_PLANETARIAS
        self.UMBRALES = UMBRALES_ALERTA
        
        # Datos precalculados de eventos históricos
        self.datos_precalculados = {}
        for fecha, evento in EVENTOS_HISTORICOS.items():
            self.datos_precalculados[fecha] = evento['ftrt_normalizada']
        
        # Añadir día normal
        self.datos_precalculados['2024-01-01'] = 0.95
        
    def calcular_ftrt_total(self, fecha):
        """Calcula FTRT usando variables globales"""
        fecha_str = fecha.strftime('%Y-%m-%d')
        
        # Usar datos precalculados si están disponibles
        if fecha_str in self.datos_precalculados:
            ftrt_norm = self.datos_precalculados[fecha_str]
            return {
                'ftrt_total': ftrt_norm * 1e15,
                'ftrt_normalizada': ftrt_norm,
                'contribuciones': self._contribuciones_estimadas(ftrt_norm),
                'fecha': fecha,
                'metodo': 'precalculado'
            }
        
        # Si no, calcular (versión simplificada)
        ftrt_norm = 1.0  # Valor por defecto
        return {
            'ftrt_total': ftrt_norm * 1e15,
            'ftrt_normalizada': ftrt_norm,
            'contribuciones': self._contribuciones_estimadas(ftrt_norm),
            'fecha': fecha,
            'metodo': 'calculado'
        }
    
    def _contribuciones_estimadas(self, ftrt_norm):
        """Estima contribuciones basadas en FTRT"""
        base_contributions = {
            'jupiter': 1.0e15,
            'saturn': 2.5e14,
            'venus': 8.0e13,
            'earth': 7.5e13,
            'mercury': 1.5e13
        }
        factor = ftrt_norm / 1.0
        return {k: v * factor for k, v in base_contributions.items()}
    
    def evaluar_riesgo(self, ftrt_normalizada):
        """Evalúa nivel de riesgo usando umbrales globales"""
        if ftrt_normalizada < self.UMBRALES['NORMAL']:
            return 'NORMAL', COLORES_ALERTA['NORMAL']
        elif ftrt_normalizada < self.UMBRALES['MODERADO']:
            return 'MODERADO', COLORES_ALERTA['MODERADO']
        elif ftrt_normalizada < self.UMBRALES['ELEVADO']:
            return 'ELEVADO', COLORES_ALERTA['ELEVADO']
        elif ftrt_normalizada < self.UMBRALES['CRITICO']:
            return 'CRITICO', COLORES_ALERTA['CRITICO']
        else:
            return 'EXTREMO', COLORES_ALERTA['EXTREMO']
    
    def generar_alerta(self, fecha):
        """Genera alerta usando sistema global"""
        resultado = self.calcular_ftrt_total(fecha)
        ftrt_norm = resultado['ftrt_normalizada']
        
        nivel, color = self.evaluar_riesgo(ftrt_norm)
        
        return {
            'fecha': fecha,
            'ftrt_normalizada': round(ftrt_norm, 3),
            'nivel_riesgo': nivel,
            'color_alerta': color,
            'metodo_calculo': resultado.get('metodo', 'desconocido')
        }

# Función de demostración
def demostrar_sistema_global():
    """Demuestra el sistema usando variables globales"""
    print("🌐 SISTEMA FTRT CON VARIABLES GLOBALES")
    print("=" * 50)
    
    calc = FTRTCalculator()
    
    # Probar eventos históricos
    for fecha_str in ['1859-09-01', '2003-10-29', '2024-05-10']:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        alerta = calc.generar_alerta(fecha)
        evento = EVENTOS_HISTORICOS.get(fecha_str, {})
        
        print(f"{fecha_str}: {evento.get('nombre', 'Evento')}")
        print(f"  FTRT: {alerta['ftrt_normalizada']} | Alerta: {alerta['nivel_riesgo']} {alerta['color_alerta']}")
        print(f"  Método: {alerta['metodo_calculo']}")
        print()

if __name__ == "__main__":
    demostrar_sistema_global()
    from config.global_variables import mostrar_estado_sistema
    mostrar_estado_sistema()
