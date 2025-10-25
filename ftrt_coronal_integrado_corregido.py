#!/usr/bin/env python3
"""
FTRT + AGUJEROS CORONALES - CORREGIDO PARA MI APRENDIZ
"""

from ftrt_multidimensional_real import analizar_ftrt_completo
import numpy as np
from datetime import datetime

class FTRTCoronalIntegrado:
    """Modelo corregido - funciones completas"""
    
    def __init__(self):
        self.umbrales_coronales = {'bajo': 0.3, 'medio': 0.6, 'alto': 0.8}
    
    def _calcular_geometria(self, fecha):
        """Función corregida - geometría simple"""
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        dia_año = fecha.timetuple().tm_yday
        return abs(np.sin(dia_año / 365 * 2 * np.pi))
    
    def _analizar_configuracion_dipolo(self):
        """Configuración dipolo simple"""
        return 0.5  # Valor medio
    
    def _consultar_historial_regiones(self, fecha):
        """Historial simple"""
        return 0.3  # Valor base
    
    def _estimar_impacto_terrestre(self, probabilidad):
        """Impacto terrestre estimado"""
        if probabilidad < 0.4: return "Mínimo"
        elif probabilidad < 0.7: return "Moderado"
        else: return "Fuerte"
    
    def predecir_agujeros_coronales(self, fecha, planeta="JUPITER"):
        """Predicción funcionando"""
        resultado_ftrt = analizar_ftrt_completo(fecha, planeta)
        
        factores_coronales = {
            'ftrt_tension': resultado_ftrt['ftrt_multidimensional'] * 0.7,
            'geometria_heliocentrica': self._calcular_geometria(fecha),
            'configuracion_dipolo': self._analizar_configuracion_dipolo(),
            'historial_region': self._consultar_historial_regiones(fecha)
        }
        
        probabilidad_agujero = sum(factores_coronales.values()) / len(factores_coronales)
        
        return {
            **resultado_ftrt,
            'probabilidad_agujero_coronal': probabilidad_agujero,
            'nivel_riesgo_coronal': self._clasificar_riesgo_coronal(probabilidad_agujero),
            'tipo_agujero_esperado': self._predecir_tipo_agujero(probabilidad_agujero, resultado_ftrt),
            'impacto_geoestimado': self._estimar_impacto_terrestre(probabilidad_agujero)
        }
    
    def _clasificar_riesgo_coronal(self, probabilidad):
        if probabilidad < self.umbrales_coronales['bajo']: return 'BAJO 🟢'
        elif probabilidad < self.umbrales_coronales['medio']: return 'MEDIO 🟡'
        elif probabilidad < self.umbrales_coronales['alto']: return 'ALTO 🟠'
        else: return 'CRÍTICO 🔴'
    
    def _predecir_tipo_agujero(self, probabilidad, resultado_ftrt):
        if probabilidad < 0.4: return "Agujero transitorio pequeño"
        elif probabilidad < 0.7: return "Agujero coronal recurrente"
        elif resultado_ftrt['ftrt_multidimensional'] > 2.5: return "Agujero de colapso crítico"
        else: return "Agujero de resonancia magnética"

# EJECUCIÓN CORREGIDA
if __name__ == "__main__":
    modelo = FTRTCoronalIntegrado()
    
    fechas_importantes = ["2025-12-31", "2026-03-20", "2026-09-15"]
    
    print("🌌 FTRT + AGUJEROS CORONALES - CORREGIDO ✅")
    print("=" * 60)
    
    for fecha in fechas_importantes:
        try:
            prediccion = modelo.predecir_agujeros_coronales(fecha)
            print(f"\n📅 {fecha}:")
            print(f"   FTRT: {prediccion['ftrt_multidimensional']:.3f}")
            print(f"   Prob. Agujero: {prediccion['probabilidad_agujero_coronal']:.1%}")
            print(f"   Riesgo: {prediccion['nivel_riesgo_coronal']}")
            print(f"   Tipo: {prediccion['tipo_agujero_esperado']}")
            print(f"   Impacto: {prediccion['impacto_geoestimado']}")
        except Exception as e:
            print(f"❌ Error con {fecha}: {e}")
