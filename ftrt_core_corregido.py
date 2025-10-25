"""
FTRT CORE CORREGIDO - Versión fácil para mi Aprendiz
"""

import numpy as np
from datetime import datetime, timedelta
import ephem

# =============================================================================
# CLASE BASE FTRT (ORIGINAL)
# =============================================================================

class FTRTCalculator:
    def __init__(self):
        self.R_SOL = 6.957e8
        self.UA = 1.496e11
        self.MASAS = {
            'mercury': 3.3011e23, 'venus': 4.8675e24, 'earth': 5.9722e24,
            'mars': 6.4171e23, 'jupiter': 1.8982e27, 'saturn': 5.6834e26,
            'uranus': 8.6810e25, 'neptune': 1.0241e26
        }
    
    def calcular_ftrt_total(self, fecha):
        """Versión CORREGIDA - acepta string o datetime"""
        # Convertir string a datetime si es necesario
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        
        ftrt_total = 0
        contribuciones = {}
        
        for planeta in self.MASAS.keys():
            try:
                # Cálculo simplificado para prueba
                ftrt_individual = self._calcular_ftrt_simple(planeta, fecha)
                ftrt_total += ftrt_individual
                contribuciones[planeta] = ftrt_individual
            except:
                contribuciones[planeta] = 0
        
        # Normalizar respecto a Júpiter
        ftrt_jupiter = contribuciones.get('jupiter', 1)
        ftrt_normalizada = ftrt_total / ftrt_jupiter if ftrt_jupiter > 0 else 0
        
        return {
            'ftrt_total': ftrt_total,
            'ftrt_normalizada': ftrt_normalizada,
            'contribuciones': contribuciones,
            'fecha': fecha
        }
    
    def _calcular_ftrt_simple(self, planeta, fecha):
        """Cálculo simplificado para pruebas"""
        # Valores base por planeta
        bases = {
            'mercury': 0.8, 'venus': 1.2, 'earth': 1.0,
            'mars': 0.5, 'jupiter': 3.0, 'saturn': 2.0,
            'uranus': 0.3, 'neptune': 0.2
        }
        
        base = bases.get(planeta, 0.1)
        
        # Variación basada en día del año
        dia_del_ano = fecha.timetuple().tm_yday
        variacion = np.sin(dia_del_ano / 365 * 2 * np.pi) * 0.5 + 1
        
        return base * variacion

# =============================================================================
# NUEVO FTRT MULTIDIMENSIONAL (CORREGIDO)
# =============================================================================

class FTRTMultidimensional:
    """Modelo FTRT expandido - VERSIÓN CORREGIDA"""
    
    def __init__(self):
        self.planetas_disparadores = {
            'MARTE': {'peso': 1.2, 'rol': 'Activador rápido'},
            'VENUS': {'peso': 1.1, 'rol': 'Modulador frecuencia'}, 
            'JUPITER': {'peso': 1.5, 'rol': 'Amplificador escala'},
            'SATURNO': {'peso': 1.3, 'rol': 'Estructurador patrones'}
        }
    
    def calcular_alineacion_directa(self, planeta, fecha):
        """Calcula alineación planeta-región activa"""
        # Asegurar que fecha es datetime
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        
        # Posición básica del planeta
        posiciones = {
            'MARTE': {'max_alineacion': 15, 'periodo': 687},
            'VENUS': {'max_alineacion': 12, 'periodo': 225},
            'JUPITER': {'max_alineacion': 25, 'periodo': 4333},
            'SATURNO': {'max_alineacion': 20, 'periodo': 10759}
        }
        
        if planeta in posiciones:
            config = posiciones[planeta]
            dia_del_ano = fecha.timetuple().tm_yday
            alineacion = abs(np.sin(dia_del_ano / config['periodo'] * 2 * np.pi)) * config['max_alineacion']
            
            return {
                'planeta': planeta,
                'alineacion': alineacion,
                'factor_impacto': alineacion * self.planetas_disparadores[planeta]['peso'],
                'fecha': fecha.strftime('%Y-%m-%d')
            }
        return None
    
    def calcular_ftrt_multidimensional(self, fecha, planeta_principal=None):
        """Calcula FTRT multidimensional - VERSIÓN CORREGIDA"""
        
        # Asegurar fecha correcta
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        
        # FTRT base
        calc_base = FTRTCalculator()
        resultado_base = calc_base.calcular_ftrt_total(fecha)
        ftrt_base = resultado_base['ftrt_normalizada']
        
        # Factor de alineación
        factor_alineacion = 1.0
        if planeta_principal:
            alineacion = self.calcular_alineacion_directa(planeta_principal, fecha)
            if alineacion:
                factor_alineacion = 1.0 + (alineacion['factor_impacto'] / 100)
        
        # FTRT multidimensional
        ftrt_multidimensional = ftrt_base * factor_alineacion
        
        return {
            'fecha': fecha.strftime('%Y-%m-%d'),
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
# FUNCIONES FÁCILES CORREGIDAS
# =============================================================================

def ftmt_rapido(fecha, planeta=None):
    """Función rápida CORREGIDA"""
    calculador = FTRTMultidimensional()
    return calculador.calcular_ftrt_multidimensional(fecha, planeta)

def analizar_configuracion_especial(fecha):
    """Analiza configuración planetaria especial - CORREGIDA"""
    calculador = FTRTMultidimensional()
    
    resultados = {}
    for planeta in ['MARTE', 'VENUS', 'JUPITER', 'SATURNO']:
        resultados[planeta] = calculador.calcular_alineacion_directa(planeta, fecha)
    
    return resultados

# =============================================================================
# PRUEBA INMEDIATA
# =============================================================================

if __name__ == "__main__":
    print("🚀 FTRT MULTIDIMENSIONAL - VERSIÓN CORREGIDA")
    print("=" * 50)
    
    # Pruebas con strings (fácil)
    fechas_prueba = ['2025-10-25', '2003-10-29', '2024-05-10']
    
    for fecha in fechas_prueba:
        print(f"\n📅 FECHA: {fecha}")
        resultado = ftmt_rapido(fecha, 'JUPITER')
        print(f"   FTRT Base: {resultado['ftrt_base']:.3f}")
        print(f"   FTRT Multi: {resultado['ftrt_multidimensional']:.3f}")
        print(f"   🚨 {resultado['nivel_riesgo']}")
        
        print("   🪐 Alineaciones:")
        analisis = analizar_configuracion_especial(fecha)
        for p, d in analisis.items():
            if d: 
                emoji = "🟢" if d['alineacion'] < 5 else "🟡" if d['alineacion'] < 10 else "🟠" if d['alineacion'] < 15 else "🔴"
                print(f"     {p}: {d['alineacion']:5.1f}% {emoji}")
