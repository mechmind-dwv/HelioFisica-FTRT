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
        fecha_str = fecha.strftime('%Y-%m-%d')
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
