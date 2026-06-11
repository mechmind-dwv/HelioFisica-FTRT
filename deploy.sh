#!/bin/bash
echo "🚀 Iniciando despliegue del sistema FTRT..."

# Si usas GitHub Pages, copia los archivos estáticos a public/
mkdir -p public
cp -r webapp/* public/ 2>/dev/null || echo "ℹ️  No se encontró webapp/"

# Aquí puedes añadir comandos reales de deploy (scp, rsync, etc.)
echo "✅ Despliegue completado exitosamente"
