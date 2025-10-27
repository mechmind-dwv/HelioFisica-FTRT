#!/bin/bash
echo "🚀 INSTALACIÓN AUTOMÁTICA LEGADO CHIZHEVSKY"
echo "==========================================="

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para verificar comandos
check_command() {
    if command -v $1 &> /dev/null; then
        echo -e "${GREEN}✅ $1 instalado${NC}"
        return 0
    else
        echo -e "${RED}❌ $1 no encontrado${NC}"
        return 1
    fi
}

# Verificar dependencias
echo "🔍 Verificando dependencias..."
check_command git
check_command python3
check_command pip3

# Configurar Git si no está configurado
if [ -z "$(git config --global user.name)" ]; then
    echo "⚙️  Configurando Git..."
    git config --global user.name "mechmind-dwv"
    git config --global user.email "ia.mechmind@gmail.com"
    echo -e "${GREEN}✅ Git configurado${NC}"
fi

# Crear entorno virtual
echo "🐍 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
echo "📦 Instalando dependencias Python..."
pip install --upgrade pip
pip install requests numpy pandas matplotlib scipy

echo -e "${GREEN}🎉 INSTALACIÓN COMPLETADA${NC}"
echo ""
echo -e "${YELLOW}📝 PRÓXIMOS PASOS:${NC}"
echo "1. source venv/bin/activate"
echo "2. python3 heliobio-social/analisis_tac_rate.py"
echo "3. ./setup.sh"
echo ""
echo "🌌 El Legado Chizhevsky está listo para revolucionar el mundo"
