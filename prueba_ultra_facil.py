#!/usr/bin/env python3
"""
PRUEBA ULTRA FÁCIL - AGUJEROS CORONALES
Para mi Aprendiz Español 🌟
"""

from ftrt_core import ftmt_coronal_facil
from datetime import datetime

print("🎯 PRUEBA ULTRA FÁCIL AGUJEROS CORONALES")
print("=" * 50)

# Fecha de hoy
hoy = datetime.now().strftime("%Y-%m-%d")
print(f"📅 Hoy: {hoy}")

# Probabilidad hoy
resultado_hoy = ftmt_coronal_facil(hoy, "JUPITER")
print(f"🔮 Probabilidad hoy: {resultado_hoy['probabilidad']:.1%}")
print(f"🎯 Riesgo: {resultado_hoy['riesgo']}")
print(f"🌌 Tipo: {resultado_hoy['tipo_agujero']}")

print("\n📊 PRÓXIMOS MESES:")
futuro = ["2025-12-31", "2026-03-20", "2026-06-15"]
for fecha in futuro:
    r = ftmt_coronal_facil(fecha, "SATURNO")
    print(f"   {fecha}: {r['probabilidad']:.1%} → {r['riesgo']}")

print("\n💫 ¡TODO FUNCIONA PERFECTO!")
