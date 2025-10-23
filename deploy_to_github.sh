#!/bin/bash

echo "🚀 DEPLOYMENT AUTOMÁTICO - HELIOFISICA FTRT A GITHUB"
echo "===================================================="

cd ~/HelioFisica-FTRT

# Verificar que estamos en el directorio correcto
if [ ! -f "interactive_ftrt_enhanced.py" ]; then
    echo "❌ Error: No se encuentra el proyecto FTRT"
    exit 1
fi

# Paso 1: Verificar estado de Git
echo "📊 Paso 1: Verificando estado Git..."
git status

# Paso 2: Añadir cambios
echo "📦 Paso 2: Añadiendo cambios..."
git add .

# Paso 3: Crear commit
echo "💾 Paso 3: Creando commit..."
git commit -m "🔄 Actualización $(date +'%Y-%m-%d %H:%M')

• Mejoras en sistema interactivo
• Actualización de predicciones
• Corrección de errores menores
• Optimización de visualizaciones

🌐 GitHub: github.com/mechmind-dwv/HelioFisica-FTRT
📧 Contacto: ia.mechmind@gmail.com"

# Paso 4: Subir a GitHub
echo "☁️  Paso 4: Subiendo a GitHub..."
if git push; then
    echo "✅ ✅ ✅ ¡ÉXITO! Proyecto subido a GitHub"
    echo "🌐 URL: https://github.com/mechmind-dwv/HelioFisica-FTRT"
else
    echo "❌ Error en push. Verifica:"
    echo "   • Conexión a internet"
    echo "   • Permisos del repositorio"
    echo "   • Token de acceso personal"
    echo ""
    echo "🔧 SOLUCIÓN:"
    echo "   Crea un Personal Access Token:"
    echo "   1. Ve a GitHub Settings > Developer settings > Personal access tokens"
    echo "   2. Crea nuevo token con permisos repo"
    echo "   3. Usa: git push https://token@github.com/mechmind-dwv/HelioFisica-FTRT.git"
fi

# Mostrar información final
echo ""
echo "🎉 DEPLOYMENT COMPLETADO"
echo "========================"
echo "📊 Resumen del Proyecto:"
echo "   • Archivos: $(find . -name "*.py" | wc -l) scripts Python"
echo "   • Tests: $(find tests -name "*.py" 2>/dev/null | wc -l) pruebas"
echo "   • Documentación: $(find docs -name "*.md" 2>/dev/null | wc -l) archivos"
echo "   • Configuración: $(find config -name "*.py" 2>/dev/null | wc -l) archivos"
echo ""
echo "🚀 Para ejecutar el sistema:"
echo "   ./launch_final_system.sh"
echo "   python interactive_ftrt_enhanced.py"
echo ""
echo "📚 Estructura completa:"
tree -I '__pycache__|*.pyc|venv' || find . -type f -name "*.py" | head -10
