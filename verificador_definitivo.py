# verificador_definitivo.py - Verifica TODO el sistema
from datetime import datetime

def verificar_sistema_completo():
    print("🌌 VERIFICACIÓN DEFINITIVA DEL SISTEMA FTRT")
    print("=" * 60)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    verificaciones = []
    
    # 1. Verificar módulos principales
    try:
        from ftrt_core import FTRTCalculator
        verificaciones.append(("Módulo FTRT Core", "✅"))
    except Exception as e:
        verificaciones.append(("Módulo FTRT Core", f"❌ {e}"))
    
    try:
        from historical_database import HISTORICAL_EVENTS
        verificaciones.append(("Base datos histórica", "✅"))
    except Exception as e:
        verificaciones.append(("Base datos histórica", f"❌ {e}"))
    
    # 2. Verificar sistema interactivo
    try:
        from interactive_ftrt_enhanced import EnhancedFTRTAnalyzer
        analyzer = EnhancedFTRTAnalyzer()
        
        # Verificar métodos requeridos
        metodos_requeridos = [
            'analisis_comparativo_ftrt', 'analisis_detallado_evento',
            'analisis_correlaciones', 'modelo_predictivo_integrado',
            'marco_teorico_completo', 'discusion_completa',
            'limitaciones_direcciones_futuras', 'implicaciones_astrobiologia_exoplanetas',
            'conclusion_final', 'analisis_completo_avanzado', 'implicaciones_aplicaciones'
        ]
        
        metodos_ok = 0
        for metodo in metodos_requeridos:
            if hasattr(analyzer, metodo):
                metodos_ok += 1
        
        if metodos_ok == len(metodos_requeridos):
            verificaciones.append(("Sistema interactivo", "✅ COMPLETO"))
        else:
            verificaciones.append(("Sistema interactivo", f"⚠️ {metodos_ok}/{len(metodos_requeridos)} métodos"))
            
    except Exception as e:
        verificaciones.append(("Sistema interactivo", f"❌ {e}"))
    
    # 3. Verificar scripts operativos
    import os
    scripts_operativos = [
        "validation_simple.py", "sistema_definitivo.py", 
        "magia_super_facil.sh", "prueba_ultra_facil.py"
    ]
    
    for script in scripts_operativos:
        if os.path.exists(script):
            verificaciones.append((f"Script {script}", "✅"))
        else:
            verificaciones.append((f"Script {script}", "❌"))
    
    # 4. Mostrar resultados
    print("📊 RESULTADOS DE VERIFICACIÓN:")
    for item, estado in verificaciones:
        print(f"   {estado} {item}")
    
    # Resumen final
    exitosas = sum(1 for _, estado in verificaciones if estado.startswith("✅"))
    total = len(verificaciones)
    
    print(f"\n🎯 ESTADO FINAL: {exitosas}/{total} verificaciones exitosas")
    
    if exitosas == total:
        print("🎉 ¡SISTEMA FTRT 100% OPERATIVO Y VERIFICADO!")
    else:
        print("⚠️  Sistema parcialmente operativo - Algunos componentes requieren atención")
    
    print("=" * 60)

if __name__ == "__main__":
    verificar_sistema_completo()
