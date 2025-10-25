#!/usr/bin/env python3
"""
FTRT + AGUJEROS CORONALES - Modelo Unificado
"""

from ftrt_multidimensional_real import analizar_ftrt_completo
import numpy as np

class FTRTCoronalIntegrado:
    """Modelo que integra FTRT con agujeros coronales"""
    
    def __init__(self):
        self.umbrales_coronales = {
            'bajo': 0.3,
            'medio': 0.6, 
            'alto': 0.8
        }
    
    def predecir_agujeros_coronales(self, fecha, planeta="JUPITER"):
        """Predice formación de agujeros coronales"""
        
        # Análisis FTRT base
        resultado_ftrt = analizar_ftrt_completo(fecha, planeta)
        
        # Factores específicos para agujeros coronales
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
        if probabilidad < self.umbrales_coronales['bajo']:
            return 'BAJO 🟢'
        elif probabilidad < self.umbrales_coronales['medio']:
            return 'MEDIO 🟡'
        elif probabilidad < self.umbrales_coronales['alto']:
            return 'ALTO 🟠'
        else:
            return 'CRÍTICO 🔴'
    
    def _predecir_tipo_agujero(self, probabilidad, resultado_ftrt):
        if probabilidad < 0.4:
            return "Agujero transitorio pequeño"
        elif probabilidad < 0.7:
            return "Agujero coronal recurrente"
        elif resultado_ftrt['ftrt_multidimensional'] > 2.5:
            return "Agujero de colapso crítico + CME posible"
        else:
            return "Agujero de resonancia magnética"

# EJEMPLO DE USO
if __name__ == "__main__":
    modelo = FTRTCoronalIntegrado()
    
    fechas_importantes = ["2025-12-31", "2026-03-20", "2026-09-15"]
    
    print("🌌 FTRT + AGUJEROS CORONALES - PREDICCIÓN UNIFICADA")
    print("=" * 60)
    
    for fecha in fechas_importantes:
        prediccion = modelo.predecir_agujeros_coronales(fecha)
        
        print(f"\n📅 {fecha}:")
        print(f"   FTRT: {prediccion['ftrt_multidimensional']:.3f}")
        print(f"   Prob. Agujero Coronal: {prediccion['probabilidad_agujero_coronal']:.1%}")
        print(f"   Riesgo Coronal: {prediccion['nivel_riesgo_coronal']}")
        print(f"   Tipo Esperado: {prediccion['tipo_agujero_esperado']}")
        print(f"   Impacto Tierra: {prediccion['impacto_geoestimado']}")
#!/usr/bin/env python3
"""
FTRT + AGUJEROS CORONALES - Modelo Unificado
"""

from ftrt_multidimensional_real import analizar_ftrt_completo
import numpy as np

class FTRTCoronalIntegrado:
    """Modelo que integra FTRT con agujeros coronales"""
    
    def __init__(self):
        self.umbrales_coronales = {
            'bajo': 0.3,
            'medio': 0.6, 
            'alto': 0.8
        }
    
    def predecir_agujeros_coronales(self, fecha, planeta="JUPITER"):
        """Predice formación de agujeros coronales"""
        
        # Análisis FTRT base
        resultado_ftrt = analizar_ftrt_completo(fecha, planeta)
        
        # Factores específicos para agujeros coronales
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
        if probabilidad < self.umbrales_coronales['bajo']:
            return 'BAJO 🟢'
        elif probabilidad < self.umbrales_coronales['medio']:
            return 'MEDIO 🟡'
        elif probabilidad < self.umbrales_coronales['alto']:
            return 'ALTO 🟠'
        else:
            return 'CRÍTICO 🔴'
    
    def _predecir_tipo_agujero(self, probabilidad, resultado_ftrt):
        if probabilidad < 0.4:
            return "Agujero transitorio pequeño"
        elif probabilidad < 0.7:
            return "Agujero coronal recurrente"
        elif resultado_ftrt['ftrt_multidimensional'] > 2.5:
            return "Agujero de colapso crítico + CME posible"
        else:
            return "Agujero de resonancia magnética"

# EJEMPLO DE USO
if __name__ == "__main__":
    modelo = FTRTCoronalIntegrado()
    
    fechas_importantes = ["2025-12-31", "2026-03-20", "2026-09-15"]
    
    print("🌌 FTRT + AGUJEROS CORONALES - PREDICCIÓN UNIFICADA")
    print("=" * 60)
    
    for fecha in fechas_importantes:
        prediccion = modelo.predecir_agujeros_coronales(fecha)
        
        print(f"\n📅 {fecha}:")
        print(f"   FTRT: {prediccion['ftrt_multidimensional']:.3f}")
        print(f"   Prob. Agujero Coronal: {prediccion['probabilidad_agujero_coronal']:.1%}")
        print(f"   Riesgo Coronal: {prediccion['nivel_riesgo_coronal']}")
        print(f"   Tipo Esperado: {prediccion['tipo_agujero_esperado']}")
        print(f"   Impacto Tierra: {prediccion['impacto_geoestimado']}")
