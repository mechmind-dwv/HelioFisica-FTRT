"""
Validación del Sistema FTRT Completo
"""

def validar_sistema():
    from ftrt_core import FTRTCalculator
    from case_studies import CaseStudyAnalyzer
    
    print("🧪 VALIDACIÓN DEL SISTEMA FTRT")
    print("=" * 50)
    
    # Test cálculo básico
    calc = FTRTCalculator()
    test_date = datetime(2003, 10, 29)
    resultado = calc.calcular_ftrt_total(test_date)
    
    print("✅ Cálculo FTRT funcionando")
    print(f"   FTRT Halloween 2003: {resultado['ftrt_normalizada']:.3f}")
    
    # Test casos de estudio
    analyzer = CaseStudyAnalyzer()
    comparativa = analyzer.comparative_analysis()
    
    print("✅ Análisis comparativo funcionando")
    print(f"   Eventos analizados: {len(comparativa)}")
    
    print("\n🎯 SISTEMA VALIDADO EXITOSAMENTE")

if __name__ == "__main__":
    validar_sistema()
