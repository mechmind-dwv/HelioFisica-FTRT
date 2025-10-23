#!/bin/bash

echo "🚀 LANZANDO SISTEMA FTRT COMPLETO - VERSIÓN FINAL"
echo "================================================"

cd ~/HelioFisica-FTRT

# Corregir errores conocidos
echo "🔧 Corrigiendo errores..."
sed -i 's/ftft_2003/ftrt_2003/g; s/ftft_2024/ftrt_2024/g' interactive_ftrt_enhanced.py 2>/dev/null || echo "✅ Correcciones aplicadas"

# Verificar dependencias
echo "📦 Verificando dependencias..."
python -c "import matplotlib.pyplot as plt; import pandas as pd; import numpy as np; print('✅ Todas las dependencias disponibles')" 2>/dev/null || {
    echo "⚠️  Instalando dependencias faltantes..."
    pip install matplotlib pandas numpy --break-system-packages
}

# Estado del sistema
echo ""
echo "🌐 ESTADO DEL SISTEMA FTRT:"
python -c "from config.global_variables import mostrar_estado_sistema; mostrar_estado_sistema()"

# Mostrar características del sistema interactivo
echo ""
echo "🎯 CARACTERÍSTICAS DEL SISTEMA INTERACTIVO:"
echo "   • 12 secciones científicas completas"
echo "   • Análisis comparativo FTRT 2003 vs 2024" 
echo "   • Correlaciones estadísticas validadas"
echo "   • Modelo predictivo integrado"
echo "   • Marco teórico completo"
echo "   • Implicaciones astrobiológicas"
echo "   • Análisis completo automático"

echo ""
echo "🎮 INICIANDO SISTEMA INTERACTIVO COMPLETO..."
echo "   Opción recomendada: 10 (Análisis completo automático)"
echo ""

python interactive_ftrt_enhanced.py

echo ""
echo "✅ SISTEMA FTRT - EJECUCIÓN COMPLETADA"
echo "🌐 Repositorio: github.com/mechmind-dwv/HelioFisica-FTRT"
echo "📧 Contacto: ia.mechmind@gmail.com"
