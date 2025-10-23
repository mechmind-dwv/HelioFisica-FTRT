#!/bin/bash

echo "🚀 LANZANDO SISTEMA INTERACTIVO FTRT"
echo "===================================="

cd ~/HelioFisica-FTRT

# Verificar dependencias
echo "📦 Verificando dependencias..."
python -c "import matplotlib.pyplot as plt; print('✅ Matplotlib disponible')" 2>/dev/null || {
    echo "⚠️  Instalando matplotlib..."
    pip install matplotlib --break-system-packages
}

# Estado del sistema
echo "🌐 Estado del sistema:"
python -c "from config.global_variables import mostrar_estado_sistema; mostrar_estado_sistema()"

# Lanzar sistema interactivo
echo ""
echo "🎮 Iniciando sistema interactivo..."
echo "   Opciones disponibles:"
echo "   1. 📊 Reporte completo (FTRT + Astrología)"
echo "   2. 🔍 Análisis específico por configuración"
echo "   3. 📈 Visualización comparativa" 
echo "   4. 🎯 Solo conclusiones"
echo "   5. 🚪 Salir"
echo ""

python interactive_ftrt.py
