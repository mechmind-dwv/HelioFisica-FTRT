#!/bin/bash
# install_and_run.sh

echo "🚀 INSTALANDO Y EJECUTANDO HELIOFISICA-FTRT"

# Navegar al directorio
cd ~/HelioFisica-FTRT

# Dar permisos de ejecución
chmod +x *.py
chmod +x examples/*.py
chmod +x tests/*.py

# Instalar dependencias (forzar si es necesario)
echo "📦 Instalando dependencias..."
python -m pip install numpy pandas scipy matplotlib pytest --break-system-packages

# Intentar instalar pyephem (puede fallar, no problem)
python -m pip install pyephem --break-system-packages || echo "⚠️  PyEphem no instalado, usando versión simple"

# Ejecutar tests básicos
echo "🧪 Ejecutando tests..."
python -m pytest tests/ -v || echo "⚠️  Algunos tests fallaron, continuando..."

# Ejecutar ejemplos básicos
echo "🎯 Ejecutando ejemplos..."
PYTHONPATH=. python examples/basic_usage.py
PYTHONPATH=. python examples/case_studies.py
PYTHONPATH=. python examples/predictions.py

echo "✅ INSTALACIÓN COMPLETADA"
