#!/bin/bash
echo "🚀 LANZANDO SISTEMA FTRT COMPLETO"
echo "=================================="

cd ~/HelioFisica-FTRT

# Estado del sistema
python -c "from config.global_variables import mostrar_estado_sistema; mostrar_estado_sistema()"

# Sistema principal
python ftrt_core_global.py

# Predictor avanzado
python advanced_predictor.py

echo "✅ SISTEMA FTRT OPERATIVO AL 100%"
echo "🌐 Repositorio: github.com/mechmind-dwv/HelioFisica-FTRT"
echo "📧 Contacto: ia.mechmind@gmail.com"
