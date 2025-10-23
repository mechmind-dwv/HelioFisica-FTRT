"""
Script de Verificación del Sistema FTRT
"""

from ftrt_core import FTRTCalculator
from datetime import datetime

def verificar_sistema():
    print("🔍 VERIFICACIÓN DEL SISTEMA FTRT")
    print("=" * 50)
    
    calc = FTRTCalculator()
    
    # Test 1: Eventos históricos conocidos
    print("📚 TEST 1: Eventos Históricos")
    eventos = [
        ('1859-09-01', 'Carrington', 3.21),
        ('2003-10-29', 'Halloween', 4.87),
        ('2024-05-10', 'Mayo 2024', 1.34)
    ]
    
    for fecha_str, nombre, ftrt_esperada in eventos:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        resultado = calc.calcular_ftrt_total(fecha)
        alerta = calc.generar_alerta(fecha)
        
        print(f"  {nombre} ({fecha_str}):")
        print(f"    FTRT Calculada: {resultado['ftrt_normalizada']:.3f}")
        print(f"    FTRT Esperada:  {ftrt_esperada:.3f}")
        print(f"    Alerta: {alerta['nivel_riesgo']} {alerta['color_alerta']}")
        
        # Verificar precisión
        diferencia = abs(resultado['ftrt_normalizada'] - ftrt_esperada)
        if diferencia < 0.1:
            print("    ✅ PRECISIÓN: EXCELENTE")
        elif diferencia < 0.5:
            print("    ✅ PRECISIÓN: BUENA") 
        else:
            print("    ⚠️  PRECISIÓN: REGULAR")
        print()
    
    # Test 2: Niveles de alerta
    print("🚨 TEST 2: Niveles de Alerta")
    niveles_test = [0.5, 1.0, 1.5, 2.0, 3.0]
    for ftrt in niveles_test:
        nivel, color = calc.evaluar_riesgo(ftrt)
        print(f"  FTRT {ftrt}: {nivel} {color}")
    
    print("\n✅ VERIFICACIÓN COMPLETADA")

if __name__ == "__main__":
    verificar_sistema()
