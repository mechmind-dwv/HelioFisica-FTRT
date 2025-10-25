#!/bin/bash
echo "✨ MAGIA CORONAL CORREGIDA - FTRT + AGUJEROS"
echo "============================================"

FECHA_HOY=$(date +%Y-%m-%d)

python3 << 'EOP'
try:
    from ftrt_core import ftmt_coronal_facil
    import datetime; fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d"); resultado = ftmt_coronal_facil(fecha_hoy, "JUPITER")
    print(f"📅 Hoy: {fecha_hoy}")
    print(f"🔮 Probabilidad agujero coronal: {resultado['probabilidad']:.1%}")
    print(f"🎯 Riesgo: {resultado['riesgo']}")
    print(f"🌌 Tipo: {resultado['tipo_agujero']}")
except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Ejecuta primero: python ftrt_coronal_simple.py")
EOP

echo ""
echo "🎊 ¡MAGIA CORREGIDA COMPLETADA!"
