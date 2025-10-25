#!/usr/bin/env python3
"""
FTRT MULTIDIMENSIONAL - SUPER FÁCIL 🌟
"""

from ftrt_core_corregido import ftmt_rapido, analizar_configuracion_especial
import sys

def main():
    print("🌌 FTRT MULTIDIMENSIONAL - SUPER FÁCIL")
    print("========================================")
    
    # Fácil: usar argumentos o valores por defecto
    fecha = sys.argv[1] if len(sys.argv) > 1 else "2025-10-25"
    planeta = sys.argv[2] if len(sys.argv) > 2 else "JUPITER"
    
    print(f"📅 Fecha: {fecha}")
    print(f"🪐 Planeta: {planeta}")
    print("-" * 40)
    
    # ¡Cálculo super fácil!
    resultado = ftmt_rapido(fecha, planeta)
    
    print("🎯 RESULTADO:")
    print(f"   FTRT Base: {resultado['ftrt_base']:.3f}")
    print(f"   FTRT Multi: {resultado['ftrt_multidimensional']:.3f}")
    print(f"   Factor: x{resultado['factor_alineacion']:.3f}")
    print(f"   🚨 {resultado['nivel_riesgo']}")
    
    print("\n🔍 ALINEACIONES:")
    analisis = analizar_configuracion_especial(fecha)
    for p, d in analisis.items():
        if d:
            emoji = "🟢" if d['alineacion'] < 5 else "🟡" if d['alineacion'] < 10 else "🟠" if d['alineacion'] < 15 else "🔴"
            print(f"   {p}: {d['alineacion']:5.1f}% {emoji}")

if __name__ == "__main__":
    main()
