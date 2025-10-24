#!/bin/bash

echo "🔧 CONFIGURACIÓN COMPLETA DEL ENTORNO HELIOFISICA-FTRT"
echo "======================================================"

cd ~/HelioFisica-FTRT

# Verificar Python
echo "🐍 Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no encontrado. Instala Python 3.8+ primero."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION detectado"

# Verificar pip
echo "📦 Verificando pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 no encontrado. Instálalo con: sudo apt install python3-pip"
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "ftrt_env" ]; then
    echo "🏗️ Creando entorno virtual..."
    python3 -m venv ftrt_env
fi

# Activar entorno virtual
echo "🔌 Activando entorno virtual..."
source ftrt_env/bin/activate

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Verificar instalación
echo "🧪 Verificando instalación..."
python -c "
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from config.global_variables import CONFIG_SISTEMA
    print('✅ Todas las dependencias funcionan correctamente')
    print(f'✅ Sistema FTRT v{CONFIG_SISTEMA[\"version\"]} cargado')
except ImportError as e:
    print(f'❌ Error de importación: {e}')
    exit(1)
"

# Configurar Git si no está configurado
echo "🔧 Configurando Git..."
if [ -z "$(git config user.email)" ]; then
    git config user.email "ia.mechmind@gmail.com"
    git config user.name "mechmind-dwv"
    echo "✅ Git configurado con: ia.mechmind@gmail.com"
fi

# Verificar remote de GitHub
echo "🌐 Verificando conexión GitHub..."
if git remote get-url origin &> /dev/null; then
    echo "✅ Remote origin configurado"
    git remote -v
else
    echo "⚠️  Remote origin no configurado"
    echo "   Ejecuta: ./configurar_token_github.sh"
fi

# Hacer los scripts ejecutables
chmod +x *.sh

echo ""
echo "🎉 CONFIGURACIÓN COMPLETADA"
echo "==========================="
echo "✅ Entorno virtual: ftrt_env"
echo "✅ Dependencias instaladas" 
echo "✅ Git configurado"
echo "✅ Scripts preparados"
echo ""
echo "🚀 PARA USAR EL SISTEMA:"
echo "   source ftrt_env/bin/activate    # Activar entorno"
echo "   ./launch_final_system.sh        # Sistema completo"
echo "   ./deploy_con_token.sh           # Subir a GitHub"
echo ""
echo "📚 Documentación en README.md"
