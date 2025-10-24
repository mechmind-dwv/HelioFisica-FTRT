#!/bin/bash

echo "🔍 VERIFICACIÓN RÁPIDA DE CONFIGURACIÓN GITHUB"
echo "=============================================="

cd ~/HelioFisica-FTRT

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}📊 Estado actual:${NC}"

# 1. Verificar remote URL
REMOTE_URL=$(git config --get remote.origin.url)
if [[ $REMOTE_URL == *"token"* ]]; then
    echo -e "${GREEN}✅ Token configurado en remote${NC}"
    echo "   Remote: $(echo $REMOTE_URL | sed 's/\/\/.*@/\/\/TOKEN@/')"
else
    echo -e "${YELLOW}⚠️  Remote sin token${NC}"
    echo "   Remote: $REMOTE_URL"
fi

# 2. Verificar conexión
echo -e "${YELLOW}🔗 Probando conexión...${NC}"
if git ls-remote --exit-code origin > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Conexión exitosa con GitHub${NC}"
    
    # Obtener información del repositorio
    echo -e "${YELLOW}📁 Información del repo:${NC}"
    git remote show origin | grep -E "(URL|HEAD branch)" | head -2
else
    echo -e "${RED}❌ No se puede conectar con GitHub${NC}"
    echo -e "${YELLOW}💡 Solución: Ejecuta ./configurar_token_github.sh${NC}"
fi

# 3. Verificar commits locales vs remotos
echo -e "${YELLOW}📚 Estado de commits:${NC}"
LOCAL_COMMITS=$(git log --oneline | wc -l)
echo "   Commits locales: $LOCAL_COMMITS"

# 4. Verificar si hay cambios sin commitear
if git status --porcelain | grep -q "."; then
    echo -e "${YELLOW}📦 Cambios pendientes por commit:${NC}"
    git status --porcelain
else
    echo -e "${GREEN}✅ No hay cambios pendientes${NC}"
fi

echo ""
echo -e "${YELLOW}🚀 Comandos útiles:${NC}"
echo "   ./configurar_token_github.sh  # Configurar token"
echo "   ./deploy_con_token.sh         # Hacer deployment"
echo "   git status                    # Ver estado"
echo "   git log --oneline -5          # Ver últimos commits"
