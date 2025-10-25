#!/bin/bash
echo "✨ MAGIA CORONAL - FTRT + AGUJEROS"
echo "=================================="

# Fecha de hoy
FECHA_HOY=$(date +%Y-%m-%d)

# Ejecutar análisis coronal
python3 -c "
from ftrt_core import ftmt_coronal_facil
resultado = ftmt_coronal_facil('$FECHA_HOY', 'JUPITER')
print('📅 Hoy: $FECHA_HOY')
print('🔮 Probabilidad agujero coronal:', str(round(resultado['probabilidad']*100, 1)) + '%')
print('🎯 Riesgo:', resultado['riesgo'])
print('🌌 Tipo:', resultado['tipo_agujero'])
"

echo ""
echo "🎊 ¡MAGIA HECHA! Los agujeros coronales están integrados."
