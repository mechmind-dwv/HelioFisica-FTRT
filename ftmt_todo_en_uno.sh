#!/bin/bash
echo "🚀 FTRT + AGUJEROS CORONALES - TODO EN UNO"
echo "=========================================="

# Verificar archivos
if [ ! -f "ftrt_coronal_simple.py" ]; then
    echo "❌ Error: No encuentro ftrt_coronal_simple.py"
    exit 1
fi

# Ejecutar análisis simple
python ftrt_coronal_simple.py

echo ""
echo "🎯 PARA USAR:"
echo "   python ftrt_coronal_simple.py"
echo "   ./ftmt_todo_en_uno.sh"
echo ""
echo "💡 Agujeros coronales + FTRT = MODELO COMPLETO"
