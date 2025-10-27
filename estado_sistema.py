# estado_sistema.py - Reporte completo del sistema
from datetime import datetime
import sys
import os

def generar_reporte_estado():
    """Genera reporte completo del estado del sistema FTRT"""
    
    print("🌌 REPORTE DE ESTADO - SISTEMA FTRT")
    print("=" * 60)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    # Verificar módulos principales
    modulos = {
        'FTRT Core': 'ftrt_core.py',
        'Base Datos': 'historical_database.py', 
        'Motor Predicción': 'prediction_engine.py',
        'Validación': 'validation_simple.py',
        'API': 'api/main.py',
        'Interfaz': 'interactive_ftrt.py'
    }
    
    print("📁 MÓDULOS PRINCIPALES:")
    for nombre, archivo in modulos.items():
        estado = "✅" if os.path.exists(archivo) else "❌"
        print(f"   {estado} {nombre}: {archivo}")
    
    # Verificar datos históricos
    print("\n📚 DATOS HISTÓRICOS:")
    try:
        from historical_database import HISTORICAL_EVENTS, FTRT_HISTORICAL_DATA
        print(f"   ✅ Eventos cargados: {len(HISTORICAL_EVENTS)}")
        print(f"   ✅ Datos FTRT: {len(FTRT_HISTORICAL_DATA)}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Probar cálculo básico
    print("\n🧮 CÁLCULO BÁSICO:")
    try:
        from datetime import datetime
        from ftrt_core import FTRTCalculator
        calc = FTRTCalculator()
        resultado = calc.calcular_ftrt_total(datetime.now())
        ftrt = resultado.get('ftrt_normalizada', 0)
        print(f"   ✅ FTRT actual: {ftrt:.3f}")
    except Exception as e:
        print(f"   ❌ Error cálculo: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 RECOMENDACIONES INMEDIATAS:")
    print("   1. Ejecutar: python validation_simple.py")
    print("   2. Probar: python interactive_ftrt.py") 
    print("   3. Verificar: ./magia_super_facil.sh")
    print("=" * 60)

if __name__ == "__main__":
    generar_reporte_estado()
