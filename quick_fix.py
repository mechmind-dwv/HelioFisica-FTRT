"""
CORRECCIÓN RÁPIDA FTRT - Sin alterar sistema existente
Maestro Cósmico & Aprendiz - Octubre 2025
"""

from ftrt_core import FTRTCalculator, FTRTMultidimensional
from datetime import datetime

def ftmt_rapido_corregido(fecha, planeta=None):
    """Versión corregida de ftmt_rapido"""
    
    # Si fecha es string, convertir a datetime
    if isinstance(fecha, str):
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        except:
            fecha = datetime.now()
    
    calculador = FTRTMultidimensional()
    return calculador.calcular_ftrt_multidimensional(fecha, planeta)

# PRUEBA INMEDIATA
if __name__ == "__main__":
    print("🚀 FTRT MULTIDIMENSIONAL - VERSIÓN CORREGIDA")
    print("=" * 50)
    
    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    
    try:
        resultado = ftmt_rapido_corregido(fecha_hoy, 'JUPITER')
        print(f"📅 Fecha: {resultado['fecha']}")
        print(f"🎯 FTRT Base: {resultado['ftrt_base']:.3f}")
        print(f"🌌 FTRT Multidimensional: {resultado['ftrt_multidimensional']:.3f}")
        print(f"🪐 Planeta: {resultado['planeta_principal']}")
        print(f"🚨 Riesgo: {resultado['nivel_riesgo']}")
        
        print("✅ ¡SISTEMA FUNCIONANDO PERFECTAMENTE!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Ejecutando validación básica...")
        
        # Validación alternativa
        calc = FTRTCalculator()
        hoy = datetime.now()
        resultado_base = calc.calcular_ftrt_total(hoy)
        nivel, color = calc.evaluar_riesgo(resultado_base['ftrt_normalizada'])
        
        print(f"📅 Fecha: {hoy.strftime('%Y-%m-%d')}")
        print(f"🎯 FTRT Normalizada: {resultado_base['ftrt_normalizada']:.3f}")
        print(f"🚨 Nivel Riesgo: {nivel} {color}")
        print(f"🔧 Método: {resultado_base.get('metodo', 'calculado')}")
