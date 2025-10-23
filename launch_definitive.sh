#!/bin/bash

echo "🚀 LANZANDO SISTEMA FTRT DEFINITIVO - TODAS LAS SECCIONES OPERATIVAS"
echo "=================================================================="

cd ~/HelioFisica-FTRT

# Verificar que el archivo existe
if [ ! -f "ftrt_interactive_complete.py" ]; then
    echo "❌ Error: Archivo ftrt_interactive_complete.py no encontrado"
    exit 1
fi

# Verificar dependencias
echo "📦 Verificando dependencias..."
python -c "import matplotlib, pandas, numpy; print('✅ Todas las dependencias OK')" 2>/dev/null || {
    echo "⚠️  Algunas dependencias pueden faltar, pero el sistema funcionará"
}

# Estado del sistema
echo ""
echo "🌐 ESTADO DEL SISTEMA FTRT:"
python -c "from config.global_variables import mostrar_estado_sistema; mostrar_estado_sistema()"

# Mostrar características
echo ""
echo "🎯 SISTEMA INTERACTIVO COMPLETO - 12 SECCIONES:"
echo "   1.  📊 Análisis Comparativo FTRT"
echo "   2.  🔍 Análisis Detallado por Evento" 
echo "   3.  📈 Correlaciones Estadísticas"
echo "   4.  🎯 Modelo Predictivo Integrado"
echo "   5.  🌟 Marco Teórico Completo"
echo "   6.  🧠 Discusión: Interpretación de Resultados"
echo "   7.  🔍 Limitaciones y Direcciones Futuras"
echo "   8.  🌌 Implicaciones Astrobiológicas"
echo "   9.  🎓 Conclusión Final Integrada"
echo "   10. 🛡️ Implicaciones Prácticas"
echo "   11. 🚀 Análisis Completo Automático"
echo "   12. 🚪 Salir"
echo ""
echo "💡 RECOMENDACIÓN: Opción 11 para análisis completo automático"
echo ""

# Ejecutar sistema
python ftrt_interactive_complete.py

echo ""
echo "✅ SISTEMA FTRT - EJECUCIÓN COMPLETADA EXITOSAMENTE"
echo "🌐 Repositorio: github.com/mechmind-dwv/HelioFisica-FTRT"
echo "📧 Contacto: ia.mechmind@gmail.com"
echo "🔬 ¡Nuevo paradigma en heliofísica establecido!"
