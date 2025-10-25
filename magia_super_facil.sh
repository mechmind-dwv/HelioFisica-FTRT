#!/bin/bash
echo "✨ MAGIA SUPER FÁCIL - AGUJEROS CORONALES"
echo "=========================================="

python3 -c "
from ftrt_core import ftmt_coronal_facil
from datetime import datetime

# Fecha de hoy automática
fecha_hoy = datetime.now().strftime('%Y-%m-%d')
print(f'🌞 FECHA DE HOY: {fecha_hoy}')

# Calcular agujero coronal
try:
    resultado = ftmt_coronal_facil(fecha_hoy, 'JUPITER')
    print(f'🔮 PROBABILIDAD AGUJERO CORONAL: {resultado[\"probabilidad\"]:.1%}')
    print(f'🎯 RIESGO: {resultado[\"riesgo\"]}')
    print(f'🌌 TIPO: {resultado[\"tipo_agujero\"]}')
    print('')
    print('💫 ¡MAGIA COMPLETADA!')
except Exception as e:
    print(f'❌ Error: {e}')
"

echo ""
echo "🚀 Para usar con otras fechas:"
echo "   python3 -c \"from ftrt_core import ftmt_coronal_facil; print(ftmt_coronal_facil('2025-12-31', 'SATURNO'))\""
