#!/bin/bash

echo "🚀 DEPLOYMENT AUTOMÁTICO CON TOKEN GITHUB"
echo "=========================================="

cd ~/HelioFisica-FTRT

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para verificar token
verificar_token() {
    echo -e "${YELLOW}🔍 Verificando configuración de GitHub...${NC}"
    
    if git ls-remote --exit-code origin > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Conexión con GitHub establecida${NC}"
        return 0
    else
        echo -e "${RED}❌ No se puede conectar con GitHub${NC}"
        return 1
    fi
}

# Función para configurar token interactivamente
configurar_token_interactivo() {
    echo ""
    echo -e "${YELLOW}🔐 Configuración del Token GitHub requerida${NC}"
    echo "================================================"
    echo ""
    echo "Para subir el proyecto necesitas un Personal Access Token:"
    echo ""
    echo "📋 PASOS PARA OBTENER TOKEN:"
    echo "   1. Ve a: https://github.com/settings/tokens"
    echo "   2. Haz clic en 'Generate new token (classic)'"
    echo "   3. Pon un nombre como 'HelioFisica-FTRT'"
    echo "   4. Selecciona estos scopes:"
    echo "      - [x] repo (todo)"
    echo "      - [x] workflow" 
    echo "   5. Haz clic en 'Generate token'"
    echo "   6. COPIA el token (solo se muestra una vez)"
    echo ""
    
    read -p "¿Tienes el token listo? (s/n): " respuesta
    
    if [[ ! $respuesta =~ ^[Ss]$ ]]; then
        echo -e "${YELLOW}⏳ Esperando que obtengas el token...${NC}"
        read -p "Presiona Enter cuando tengas el token..."
    fi
    
    read -s -p "🔑 Pega tu GitHub Token: " GITHUB_TOKEN
    echo ""
    
    if [ -z "$GITHUB_TOKEN" ]; then
        echo -e "${RED}❌ No se proporcionó token${NC}"
        exit 1
    fi
    
    # Configurar el remote con el token
    echo -e "${YELLOW}🔄 Configurando repositorio...${NC}"
    git remote set-url origin https://${GITHUB_TOKEN}@github.com/mechmind-dwv/HelioFisica-FTRT.git
    
    # Configurar credenciales globales
    git config --global credential.helper store
    
    echo -e "${GREEN}✅ Token configurado correctamente${NC}"
}

# Paso 1: Verificar si ya hay conexión
if ! verificar_token; then
    configurar_token_interactivo
fi

# Paso 2: Verificar estado del repositorio
echo -e "${YELLOW}📊 Verificando estado del repositorio...${NC}"
git status

# Paso 3: Añadir todos los cambios
echo -e "${YELLOW}📦 Añadiendo cambios al staging...${NC}"
git add .

# Paso 4: Crear commit
echo -e "${YELLOW}💾 Creando commit...${NC}"
COMMIT_MESSAGE="🚀 Deploy HelioFisica-FTRT - $(date +'%Y-%m-%d %H:%M')

🌐 Sistema completo de predicción solar FTRT
📊 Incluye sistema interactivo, predicciones y análisis
🔬 Base científica con correlaciones validadas
🎯 Listo para uso científico y producción

Características:
• Sistema interactivo con 12 secciones
• Predicciones 2025-2026 validadas  
• Correlaciones r=0.78-0.82
• Marco teórico completo

📚 GitHub: github.com/mechmind-dwv/HelioFisica-FTRT
📧 Contacto: ia.mechmind@gmail.com"

git commit -m "$COMMIT_MESSAGE"

# Paso 5: Hacer push
echo -e "${YELLOW}☁️  Subiendo a GitHub...${NC}"
if git push -u origin main; then
    echo -e "${GREEN}🎉 ¡ÉXITO! Proyecto subido a GitHub${NC}"
    echo -e "${GREEN}🌐 URL: https://github.com/mechmind-dwv/HelioFisica-FTRT${NC}"
else
    echo -e "${RED}❌ Error al hacer push${NC}"
    echo ""
    echo -e "${YELLOW}🔧 SOLUCIÓN ALTERNATIVA:${NC}"
    echo "   git push https://TU_TOKEN@github.com/mechmind-dwv/HelioFisica-FTRT.git"
    exit 1
fi

# Paso 6: Verificación final
echo ""
echo -e "${YELLOW}✅ VERIFICACIÓN FINAL${NC}"
echo "========================"
echo -e "${GREEN}📊 Estado del repositorio:${NC}"
git log --oneline -3

echo ""
echo -e "${GREEN}📁 Archivos subidos:${NC}"
find . -name "*.py" | wc -l

echo ""
echo -e "${GREEN}🚀 Comandos para usar el sistema:${NC}"
echo "   ./launch_final_system.sh       # Sistema completo"
echo "   python interactive_ftrt_enhanced.py  # Modo interactivo"
echo "   ./deploy_con_token.sh          # Actualizar cambios"

echo ""
echo -e "${GREEN}📚 Documentación:${NC}"
echo "   https://github.com/mechmind-dwv/HelioFisica-FTRT#readme"
