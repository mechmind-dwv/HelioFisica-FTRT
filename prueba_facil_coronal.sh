#!/bin/bash
echo "🎯 PRUEBA FÁCIL AGUJEROS CORONALES"
echo "=================================="

python3 << 'EOP'
from ftrt_coronal_integrado_corregido import FTRTCoronalIntegrado

modelo = FTRTCoronalIntegrado()
print("🔥 PREDICCIÓN AGUJEROS CORONALES 2025-2026:")

fechas = ['2025-12-31', '2026-03-20', '2026-09-15']
for fecha in fechas:
    try:
        p = modelo.predecir_agujeros_coronales(fecha)
        prob = p['probabilidad_agujero_coronal']
        riesgo = p['nivel_riesgo_coronal']
        print(f"{fecha}: {prob:.1%} → {riesgo}")
    except Exception as e:
        print(f"{fecha}: Error - {e}")
EOP

echo ""
echo "✅ ¡Prueba completada!"
