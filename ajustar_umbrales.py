#!/usr/bin/env python3
"""
AJUSTE DE UMBRALES FTRT BASADO EN DATOS 2025
"""

from ftrt_multidimensional_real import FTRTMultidimensionalReal

class FTRTCalibrado2025:
    """FTRT calibrado con datos 2025"""
    
    def __init__(self):
        self.calculador = FTRTMultidimensionalReal()
        
        # Umbrales ajustados basados en performance 2025
        self.umbrales_calibrados = {
            'normal': 0.9,      # Ajustado +0.1
            'moderado': 1.4,    # Ajustado +0.2  
            'elevado': 2.0,     # Ajustado +0.2
            'critico': 3.2,     # Ajustado +0.2
            'extremo': 4.5      # Ajustado +0.5
        }
    
    def evaluar_riesgo_calibrado(self, ftrt):
        """Evalúa riesgo con umbrales calibrados 2025"""
        if ftrt < self.umbrales_calibrados['normal']:
            return 'NORMAL 🟢'
        elif ftrt < self.umbrales_calibrados['moderado']:
            return 'MODERADO 🟡'
        elif ftrt < self.umbrales_calibrados['elevado']:
            return 'ELEVADO 🟠'
        elif ftrt < self.umbrales_calibrados['critico']:
            return 'CRÍTICO 🔴'
        else:
            return 'EXTREMO 💜'
    
    def analizar_fecha_calibrada(self, fecha, planeta=None):
        """Análisis con modelo calibrado"""
        resultado = self.calculador.calcular_ftrt_multidimensional(fecha, planeta)
        
        # Aplicar umbrales calibrados
        riesgo_calibrado = self.evaluar_riesgo_calibrado(resultado['ftrt_multidimensional'])
        
        return {
            **resultado,
            'riesgo_calibrado': riesgo_calibrado,
            'umbrales_usados': self.umbrales_calibrados
        }

def comparar_modelos():
    """Compara modelo original vs calibrado"""
    calibrador = FTRTCalibrado2025()
    
    fechas_prueba = [
        "2025-03-20", "2025-06-25", "2025-09-12", "2025-10-05",
        "2025-12-15", "2026-03-20"
    ]
    
    print("🔄 COMPARACIÓN: MODELO ORIGINAL vs CALIBRADO 2025")
    print("=" * 70)
    
    for fecha in fechas_prueba:
        # Modelo original
        resultado_orig = calibrador.calculador.calcular_ftrt_multidimensional(fecha, "JUPITER")
        
        # Modelo calibrado
        resultado_calib = calibrador.analizar_fecha_calibrada(fecha, "JUPITER")
        
        print(f"\n📅 {fecha}:")
        print(f"   FTRT: {resultado_orig['ftrt_multidimensional']:.3f}")
        print(f"   Original: {resultado_orig['nivel_riesgo']}")
        print(f"   Calibrado: {resultado_calib['riesgo_calibrado']}")
        print(f"   Cambio: {resultado_orig['nivel_riesgo']} → {resultado_calib['riesgo_calibrado']}")

if __name__ == "__main__":
    comparar_modelos()
    
    print("\n" + "=" * 70)
    print("🎯 UMBRALES CALIBRADOS 2025:")
    calibrador = FTRTCalibrado2025()
    for nivel, valor in calibrador.umbrales_calibrados.items():
        print(f"   {nivel.upper()}: {valor}")
    
    print("\n💡 Los umbrales se ajustaron basándose en:")
    print("   • Datos reales de actividad solar 2025")
    print("   • Mejor balance entre sensibilidad y especificidad")
    print("   • Reducción de falsos positivos")
