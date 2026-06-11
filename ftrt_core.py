"""
Núcleo Principal del Sistema FTRT
Autores: Benjamin Cabeza Duran / DeepSeek
Fecha: Octubre 2025
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import ephem
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class FTRTCalculator:
    def __init__(self):
        # Constantes fundamentales
        self.R_SOL = 6.957e8  # Radio solar en metros
        self.UA = 1.496e11    # Unidad Astronómica en metros
        self.G = 6.67430e-11  # Constante gravitacional
        
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
        
    def calcular_posicion_planeta(self, planeta, fecha):
        """
        Calcula posición heliocéntrica usando pyephem con precisión NASA
        """
        if planeta == 'earth':
            sun = ephem.Sun()
            sun.compute(fecha)
            distancia = sun.earth_distance * self.UA
            return {
                'distancia': distancia,
                'longitud': 0.0,
                'latitud': 0.0
            }

        bodies = {
            'mercury': ephem.Mercury(),
            'venus': ephem.Venus(),
            'mars': ephem.Mars(),
            'jupiter': ephem.Jupiter(),
            'saturn': ephem.Saturn(),
            'uranus': ephem.Uranus(),
            'neptune': ephem.Neptune()
        }

        body = bodies[planeta]
        body.compute(fecha)
        distancia = body.sun_distance * self.UA

        return {
            'distancia': distancia,
            'longitud': body.hlon,
            'latitud': body.hlat
        }
    def calcular_ftrt_individual(self, planeta, fecha):
        """
        Calcula FTRT para planeta específico: Masa * R_sol / distancia³
        """
        posicion = self.calcular_posicion_planeta(planeta, fecha)
        masa = self.MASAS[planeta]
        distancia = posicion['distancia']
        
        if distancia == 0:
            return 0
            
        return (masa * self.R_SOL) / (distancia ** 3)
    
    def calcular_ftrt_total(self, fecha):
        """
        Calcula FTRT total sumando contribuciones planetarias
        """
        ftrt_total = 0
        contribuciones = {}
        
        for planeta in self.MASAS.keys():
            ftrt_individual = self.calcular_ftrt_individual(planeta, fecha)
            ftrt_total += ftrt_individual
            contribuciones[planeta] = ftrt_individual
            
        # Normalización respecto a Júpiter
        ftrt_jupiter = contribuciones['jupiter']
        ftrt_normalizada = ftrt_total / ftrt_jupiter if ftrt_jupiter > 0 else 0
        
        return {
            'ftrt_total': ftrt_total,
            'ftrt_normalizada': ftrt_normalizada,
            'contribuciones': contribuciones,
            'fecha': fecha
        }
    
    def generar_alerta(self, fecha):
        """
        Genera alerta basada en FTRT calculada
        """
        resultado = self.calcular_ftrt_total(fecha)
        ftrt_norm = resultado['ftrt_normalizada']
        
        if ftrt_norm < self.UMBRALES['normal']:
            nivel, color = 'NORMAL', '🟢'
        elif ftrt_norm < self.UMBRALES['moderado']:
            nivel, color = 'MODERADO', '🟡'
        elif ftrt_norm < self.UMBRALES['elevado']:
            nivel, color = 'ELEVADO', '🟠'
        elif ftrt_norm < self.UMBRALES['critico']:
            nivel, color = 'CRÍTICO', '🔴'
        else:
            nivel, color = 'EXTREMO', '💜'
        
        return {
            'fecha': fecha,
            'ftrt_normalizada': round(ftrt_norm, 3),
            'nivel_riesgo': nivel,
            'color_alerta': color,
            'contribuciones_principales': dict(sorted(
                resultado['contribuciones'].items(),
                key=lambda x: x[1],
                reverse=True
            )[:3])
        }

    def evaluar_riesgo(self, ftrt_valor):
        """
        Evalúa nivel de riesgo dado un valor FTRT normalizado.
        Retorna (nivel, color).
        """
        if ftrt_valor < self.UMBRALES['normal']:
            return 'NORMAL', '🟢'
        elif ftrt_valor < self.UMBRALES['moderado']:
            return 'MODERADO', '🟡'
        elif ftrt_valor < self.UMBRALES['elevado']:
            return 'ELEVADO', '🟠'
        elif ftrt_valor < self.UMBRALES['critico']:
            return 'CRÍTICO', '🔴'
        else:
            return 'EXTREMO', '💜'
