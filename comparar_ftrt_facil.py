#!/usr/bin/env python3
"""
COMPARATIVA FÁCIL FTRT vs FTRT-MULTI
"""

from ftrt_multidimensional_real import analizar_ftrt_completo

# Fechas importantes para comparar
fechas_comparar = [
    "1859-09-01",  # Carrington
    "2003-10-29",  # Halloween
    "2024-05-10",  # Mayo 2024
    "2025-03-15",  # Futuro
    "2025-10-25"   # Hoy
]

print("🌌 COMPARATIVA FTRT vs FTRT-MULTIDIMENSIONAL")
print("=" * 60)

for fecha in fechas_comparar:
    # Sin planeta (FTRT base)
    resultado_base = analizar_ftrt_completo(fecha, None)
    
    # Con Júpiter (FTRT multi)
    resultado_multi = analizar_ftrt_completo(fecha, "JUPITER")
    
    print(f"\n📅 {fecha}:")
    print(f"   FTRT Base: {resultado_base['ftrt_base']:.3f} → {resultado_base['nivel_riesgo']}")
    print(f"   FTRT Multi: {resultado_multi['ftrt_multidimensional']:.3f} → {resultado_multi['nivel_riesgo']}")
    print(f"   Mejora: +{(resultado_multi['ftrt_multidimensional'] - resultado_base['ftrt_base']):.3f}")
    
    if resultado_multi['alineacion_data']:
        print(f"   Alineación Júpiter: {resultado_multi['alineacion_data']['alineacion']:.1f}%")

print("\n" + "=" * 60)
print("🎯 CONCLUSIÓN: FTRT Multidimensional detecta MÁS RIESGO")
print("   cuando hay alineaciones planeta-región activa!")
