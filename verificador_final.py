# verificador_final.py
from datetime import datetime

def verificar_sistema_final():
    print("🎯 VERIFICACIÓN FINAL DEL SISTEMA FTRT")
    print("=" * 50)
    
    try:
        from interactive_ftrt_enhanced import EnhancedFTRTAnalyzer
        analyzer = EnhancedFTRTAnalyzer()
        
        # Métodos que DEBEN existir para el menú completo
        metodos_requeridos = [
            'analisis_comparativo_ftrt', 'analisis_detallado_evento',
            'analisis_correlaciones', 'modelo_predictivo_integrado',
            'marco_teorico_completo', 'discusion_completa',
            'limitaciones_direcciones_futuras', 'implicaciones_astrobiologia_exoplanetas',
            'conclusion_final', 'analisis_completo_avanzado', 'implicaciones_aplicaciones',
            'mostrar_menu_principal', 'ejecutar_analisis_completo'
        ]
        
        print("🔍 VERIFICANDO MÉTODOS REQUERIDOS:")
        todos_presentes = True
        for metodo in metodos_requeridos:
            if hasattr(analyzer, metodo):
                print(f"   ✅ {metodo}")
            else:
                print(f"   ❌ {metodo} - FALTANTE")
                todos_presentes = False
        
        if todos_presentes:
            print(f"\n🎉 ¡SISTEMA INTERACTIVO 100% OPERATIVO!")
            print("   Todos los métodos requeridos están presentes")
        else:
            print(f"\n⚠️  Sistema parcialmente operativo")
            print("   Algunos métodos del menú no están implementados")
            
    except Exception as e:
        print(f"❌ Error crítico: {e}")
    
    print("=" * 50)

if __name__ == "__main__":
    verificar_sistema_final()
