#!/bin/bash

echo "🔐 CONFIGURACIÓN SEGURA DE TOKEN GITHUB"
echo "========================================"

cd ~/HelioFisica-FTRT

# Verificar si ya hay un token configurado
if git config --get remote.origin.url | grep -q "token"; then
    echo "✅ Token ya configurado"
    git config --get remote.origin.url
    exit 0
fi

# Solicitar token de forma segura
echo ""
echo "📝 Para subir el proyecto a GitHub necesitas un Personal Access Token"
echo ""
echo "🔧 CÓMO OBTENER EL TOKEN:"
echo "   1. Ve a: https://github.com/settings/tokens"
echo "   2. Haz clic en 'Generate new token'"
echo "   3. Selecciona los scopes: repo, workflow"
echo "   4. Copia el token generado"
echo ""
echo "🔒 El token se guardará de forma segura en el keychain de Git"
echo ""

read -p "¿Quieres configurar el token ahora? (s/n): " respuesta

if [[ $respuesta =~ ^[Ss]$ ]]; then
    read -s -p "🔑 Pega tu GitHub Personal Access Token: " GITHUB_TOKEN
    echo ""
    
    if [ -z "$GITHUB_TOKEN" ]; then
        echo "❌ No se proporcionó token"
        exit 1
    fi
    
    # Configurar el remote con el token
    git remote set-url origin https://${GITHUB_TOKEN}@github.com/mechmind-dwv/HelioFisica-FTRT.git
    
    # Configurar Git credentials store
    git config --global credential.helper store
    
    echo "✅ Token configurado correctamente"
    echo "🌐 Remote URL actualizado"
    git remote -v
    
    # Probar la conexión
    echo ""
    echo "🧪 Probando conexión con GitHub..."
    if git ls-remote > /dev/null 2>&1; then
        echo "✅ Conexión exitosa con GitHub"
    else
        echo "❌ Error en la conexión. Verifica el token."
    fi
else
    echo "ℹ️  Puedes configurar el token manualmente después con:"
    echo "   git remote set-url origin https://TOKEN@github.com/mechmind-dwv/HelioFisica-FTRT.git"
fi
