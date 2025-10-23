"""
Sistema de Predicción FTRT v2.0
Autores: Benjamin Cabeza Duran / DeepSeek
Licencia: MIT
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
        
        # Masas planetarias (kg)
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
        
        # Umbrales de alerta
        self.UMBRALES = {
            'normal': 0.8,
            'moderado': 1.2,
            'elevado': 1.8,
            'critico': 2.5
        }
        
    def calcular_posicion_planeta(self, planeta, fecha):
        """
        Calcula posición heliocéntrica usando pyephem
        """
        bodies = {
            'mercury': ephem.Mercury(),
            'venus': ephem.Venus(),
            'earth': ephem.Earth(),
            'mars': ephem.Mars(),
            'jupiter': ephem.Jupiter(),
            'saturn': ephem.Saturn(),
            'uranus': ephem.Uranus(),
            'neptune': ephem.Neptune()
        }
        
        body = bodies[planeta]
        body.compute(fecha)
        
        # Convertir a coordenadas heliocéntricas
        distancia_ua = body.earth_distance
        longitud = body.hlon
        latitud = body.hlat
        
        return {
            'distancia': distancia_ua * self.UA,  # Convertir a metros
            'longitud': longitud,
            'latitud': latitud
        }
    
    def calcular_ftrt_individual(self, planeta, fecha):
        """
        Calcula FTRT para un planeta específico
        FTRT = Masa_planeta * R_sol / distancia^3
        """
        posicion = self.calcular_posicion_planeta(planeta, fecha)
        masa = self.MASAS[planeta]
        distancia = posicion['distancia']
        
        # Evitar división por cero
        if distancia == 0:
            return 0
            
        ftrt = (masa * self.R_SOL) / (distancia ** 3)
        return ftrt
    
    def calcular_ftrt_total(self, fecha):
        """
        Calcula FTRT total sumando contribuciones de todos los planetas
        """
        ftrt_total = 0
        contribuciones = {}
        
        for planeta in self.MASAS.keys():
            ftrt_individual = self.calcular_ftrt_individual(planeta, fecha)
            ftrt_total += ftrt_individual
            contribuciones[planeta] = ftrt_individual
            
        # Normalizar respecto a Júpiter
        ftrt_jupiter = contribuciones['jupiter']
        ftrt_normalizada = ftrt_total / ftrt_jupiter if ftrt_jupiter > 0 else 0
        
        return {
            'ftrt_total': ftrt_total,
            'ftrt_normalizada': ftrt_normalizada,
            'contribuciones': contribuciones,
            'fecha': fecha
        }
    
    def predecir_ftrt_rango(self, fecha_inicio, dias=30):
        """
        Predice FTRT para un rango de fechas
        """
        resultados = []
        fecha_actual = fecha_inicio
        
        for i in range(dias):
            resultado = self.calcular_ftrt_total(fecha_actual)
            resultados.append(resultado)
            fecha_actual += timedelta(days=1)
            
        return pd.DataFrame(resultados)
    
    def evaluar_riesgo(self, ftrt_normalizada):
        """
        Evalúa nivel de riesgo basado en FTRT
        """
        if ftrt_normalizada < self.UMBRALES['normal']:
            return 'NORMAL', 'Verde'
        elif ftrt_normalizada < self.UMBRALES['moderado']:
            return 'MODERADO', 'Amarillo'
        elif ftrt_normalizada < self.UMBRALES['elevado']:
            return 'ELEVADO', 'Naranja'
        elif ftrt_normalizada < self.UMBRALES['critico']:
            return 'CRÍTICO', 'Rojo'
        else:
            return 'EXTREMO', 'Púrpura'
    
    def generar_alerta(self, fecha):
        """
        Genera alerta completa para una fecha específica
        """
        resultado = self.calcular_ftrt_total(fecha)
        nivel_riesgo, color = self.evaluar_riesgo(resultado['ftrt_normalizada'])
        
        alerta = {
            'fecha': fecha,
            'ftrt_normalizada': round(resultado['ftrt_normalizada'], 3),
            'nivel_riesgo': nivel_riesgo,
            'color_alerta': color,
            'contribuciones_principales': dict(sorted(
                resultado['contribuciones'].items(),
                key=lambda x: x[1],
                reverse=True
            )[:3])
        }
        
        return alerta

class PredictorTormentas:
    """
    Clase para predicción de tormentas solares basada en FTRT
    """
    
    def __init__(self, calculador_ftrt):
        self.calculador = calculador_ftrt
        self.modelo_entrenado = False
        
    def entrenar_modelo(self, datos_historicos):
        """
        Entrena modelo de regresión para predecir probabilidad de tormenta
        """
        # Aquí iría el código de entrenamiento del modelo ML
        self.modelo_entrenado = True
        return True
    
    def predecir_tormenta(self, fecha, region_activa=None):
        """
        Predice probabilidad de tormenta solar para una fecha
        """
        resultado_ftrt = self.calculador.calcular_ftrt_total(fecha)
        ftrt_norm = resultado_ftrt['ftrt_normalizada']
        
        # Modelo simplificado de probabilidad
        if ftrt_norm < 1.0:
            probabilidad = 0.05
        elif ftrt_norm < 1.5:
            probabilidad = 0.25
        elif ftrt_norm < 2.0:
            probabilidad = 0.50
        elif ftrt_norm < 2.5:
            probabilidad = 0.75
        else:
            probabilidad = 0.95
            
        # Ajustar por presencia de región activa compleja
        if region_activa and region_activa.get('complejidad') == 'beta-gamma-delta':
            probabilidad *= 1.3
            
        return min(probabilidad, 0.99)

# EJEMPLO DE USO COMPLETO
if __name__ == "__main__":
    # Inicializar calculadora
    calculadora = FTRTCalculator()
    
    # Fecha de análisis (ejemplo: tormenta de Halloween 2003)
    fecha_analisis = datetime(2003, 10, 29)
    
    # Calcular FTRT para fecha específica
    resultado = calculadora.calcular_ftrt_total(fecha_analisis)
    
    print("=== ANÁLISIS FTRT ===")
    print(f"Fecha: {fecha_analisis.strftime('%Y-%m-%d')}")
    print(f"FTRT Total: {resultado['ftrt_total']:.2e}")
    print(f"FTRT Normalizada: {resultado['ftrt_normalizada']:.3f}")
    
    # Generar alerta
    alerta = calculadora.generar_alerta(fecha_analisis)
    print(f"\n=== ALERTA ===")
    print(f"Nivel: {alerta['nivel_riesgo']} ({alerta['color_alerta']})")
    print(f"FTRT: {alerta['ftrt_normalizada']}")
    print("Contribuciones principales:")
    for planeta, valor in alerta['contribuciones_principales'].items():
        print(f"  {planeta}: {valor:.2e}")
    
    # Predicción para próximos 30 días
    print(f"\n=== PREDICCIÓN 30 DÍAS ===")
    fecha_futuro = datetime(2025, 1, 1)
    predicciones = calculadora.predecir_ftrt_rango(fecha_futuro, 30)
    
    # Encontrar picos de riesgo
    picos = predicciones[predicciones['ftrt_normalizada'] > 1.5]
    if not picos.empty:
        print("Picos de riesgo detectados:")
        for _, pico in picos.iterrows():
            nivel, color = calculadora.evaluar_riesgo(pico['ftrt_normalizada'])
            print(f"  {pico['fecha'].strftime('%Y-%m-%d')}: FTRT={pico['ftrt_normalizada']:.2f} ({nivel})")

# FUNCIONES ADICIONALES DE EXPORTACIÓN Y ANÁLISIS
def exportar_datos_ftrt(calculador, fecha_inicio, dias, archivo_salida):
    """
    Exporta datos FTRT a CSV para análisis externo
    """
    datos = calculador.predecir_ftrt_rango(fecha_inicio, dias)
    
    # Procesar datos para exportación
    datos_export = []
    for _, fila in datos.iterrows():
        dato = {
            'fecha': fila['fecha'],
            'ftrt_total': fila['ftrt_total'],
            'ftrt_normalizada': fila['ftrt_normalizada']
        }
        # Agregar contribuciones individuales
        for planeta, valor in fila['contribuciones'].items():
            dato[f'contrib_{planeta}'] = valor
            
        datos_export.append(dato)
    
    df_export = pd.DataFrame(datos_export)
    df_export.to_csv(archivo_salida, index=False)
    print(f"Datos exportados a: {archivo_salida}")

def analisis_estadistico_avanzado(datos_ftrt):
    """
    Realiza análisis estadístico avanzado de datos FTRT
    """
    analisis = {
        'media': np.mean(datos_ftrt['ftrt_normalizada']),
        'desviacion': np.std(datos_ftrt['ftrt_normalizada']),
        'maximo': np.max(datos_ftrt['ftrt_normalizada']),
        'minimo': np.min(datos_ftrt['ftrt_normalizada']),
        'percentil_95': np.percentile(datos_ftrt['ftrt_normalizada'], 95)
    }
    
    # Detección de anomalías
    z_scores = np.abs(stats.zscore(datos_ftrt['ftrt_normalizada']))
    anomalias = datos_ftrt[z_scores > 2]
    analisis['anomalias'] = len(anomalias)
    
    return analisis

"""
INSTRUCCIONES DE USO:

1. Instalación de dependencias:
   pip install numpy pandas pyephem scipy

2. Uso básico:
   calculadora = FTRTCalculator()
   resultado = calculadora.calcular_ftrt_total(datetime(2024, 5, 10))
   alerta = calculadora.generar_alerta(datetime(2024, 5, 10))

3. Predicción de tormentas:
   predictor = PredictorTormentas(calculadora)
   probabilidad = predictor.predecir_tormenta(datetime(2025, 10, 15))

4. Exportación de datos:
   exportar_datos_ftrt(calculadora, datetime(2025, 1, 1), 365, 'ftrt_2025.csv')
"""

# Configuración para deployment en producción
class FTRTAPIService:
    """
    Servicio API para integración con sistemas de alerta temprana
    """
    
    def __init__(self):
        self.calculator = FTRTCalculator()
        self.predictor = PredictorTormentas(self.calculator)
        
    def get_alert_status(self, fecha=None):
        if fecha is None:
            fecha = datetime.now()
            
        return self.calculator.generar_alerta(fecha)
    
    def get_forecast(self, dias=30):
        fecha_inicio = datetime.now()
        return self.calculator.predecir_ftrt_rango(fecha_inicio, dias)
