#!/usr/bin/env python3
"""
SCRIPT FÁCIL FTRT MULTIDIMENSIONAL
Para mi Aprendiz Cósmico 🌟
"""

from ftrt_core import ftmt_rapido, analizar_configuracion_especial
from datetime import datetime, timedelta
import sys

def main():
    print("🌌 FTRT MULTIDIMENSIONAL - FÁCIL")
    print("=" * 40)
    
    # Fecha de hoy por defecto
    if len(sys.argv) > 1:
        fecha = sys.argv[1]
    else:
        fecha = datetime.now().strftime('%Y-%m-%d')
    
    # Planeta por defecto
    planeta = 'JUPITER' if len(sys.argv) <= 2 else sys.argv[2].upper()
    
    print(f"📅 Analizando: {fecha}")
    print(f"🪐 Planeta focus: {planeta}")
    print("-" * 40)
    
    # Cálculo principal
    resultado = ftmt_rapido(fecha, planeta)
    
    print("🎯 RESULTADO PRINCIPAL:")
    print(f"   FTRT Base: {resultado['ftrt_base']:.3f}")
    print(f"   FTRT Multi: {resultado['ftrt_multidimensional']:.3f}") 
    print(f"   Factor Alineación: x{resultado['factor_alineacion']:.3f}")
    print(f"   🚨 {resultado['nivel_riesgo']}")
    
    print("\n🔍 ALINEACIONES PLANETARIAS:")
    analisis = analizar_configuracion_especial(fecha)
    for p, d in analisis.items():
        if d:
            impacto = "🟢" if d['alineacion'] < 5 else "🟡" if d['alineacion'] < 10 else "🟠" if d['alineacion'] < 15 else "🔴"
            print(f"   {p}: {d['alineacion']:5.1f}% {impacto}")
    
    print("\n💡 EXPLICACIÓN:")
    print("   FTRT Base = Fuerza de marea baricéntrica")
    print("   FTRT Multi = Base + alineación planeta-región")
    print("   Alineación = % de alineación directa con regiones solares")

if __name__ == "__main__":
    main()
