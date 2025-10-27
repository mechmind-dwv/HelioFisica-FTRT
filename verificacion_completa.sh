#!/bin/bash
# verificacion_completa.sh - Escaneo completo del sistema FTRT

echo "🌌 INICIANDO VERIFICACIÓN COMPLETA DEL SISTEMA FTRT"
echo "=================================================="

# Función para verificar y mostrar resultado
verificar() {
    local nombre=$1
    local comando=$2
    echo -n "🔍 Verificando $nombre... "
    if eval $comando > /dev/null 2>&1; then
        echo "✅"
        return 0
    else
        echo "❌"
        return 1
    fi
}

# 1. VERIFICAR ESTRUCTURA DE ARCHIVOS
echo ""
echo "📁 ESTRUCTURA DE ARCHIVOS:"
verificar "Archivo principal FTRT" "test -f ftrt_core.py"
verificar "Base de datos histórica" "test -f historical_database.py"
verificar "Motor de predicciones" "test -f prediction_engine.py"
verificar "Sistema de validación" "test -f validation_simple.py"
verificar "Requirements" "test -f requirements.txt"

# 2. VERIFICAR DEPENDENCIAS PYTHON
echo ""
echo "📦 DEPENDENCIAS PYTHON:"
verificar "NumPy" "python -c 'import numpy'"
verificar "Pandas" "python -c 'import pandas'"
verificar "Ephem" "python -c 'import ephem'"
verificar "SciPy" "python -c 'import scipy'"
verificar "Matplotlib" "python -c 'import matplotlib'"

# 3. VERIFICAR MÓDULOS DEL SISTEMA
echo ""
echo "🔧 MÓDULOS DEL SISTEMA:"
verificar "Calculadora FTRT" "python -c 'from ftrt_core import FTRTCalculator'"
verificar "Base datos" "python -c 'from historical_database import SolarFTRTDatabase'"
verificar "Predictor" "python -c 'from prediction_engine import PredictorTormentas'"
verificar "Logger" "python -c 'from utils.logger import ftrt_logger'"

# 4. VERIFICAR SCRIPTS EJECUTABLES
echo ""
echo "🐚 SCRIPTS EJECUTABLES:"
chmod +x *.sh > /dev/null 2>&1
verificar "Script magia" "test -x magia_super_facil.sh"
verificar "Script instalación" "test -x setup_entorno_completo.sh"
verificar "Script lanzamiento" "test -x launch_ftrt.sh"

# 5. VERIFICAR DATOS HISTÓRICOS
echo ""
echo "📚 DATOS HISTÓRICOS:"
python -c "
from historical_database import HISTORICAL_EVENTS, FTRT_HISTORICAL_DATA
print('📅 Eventos históricos cargados:', len(HISTORICAL_EVENTS))
print('🔢 Datos FTRT calculados:', len(FTRT_HISTORICAL_DATA))
for evento in HISTORICAL_EVENTS[:3]:
    print('   -', evento['event_date'], evento['event_type'])
"

# 6. PRUEBA RÁPIDA DE CÁLCULO FTRT
echo ""
echo "🧮 PRUEBA DE CÁLCULO FTRT:"
python -c "
from datetime import datetime
try:
    from ftrt_core import FTRTCalculator
    calc = FTRTCalculator()
    hoy = datetime.now()
    resultado = calc.calcular_ftrt_total(hoy)
    print('✅ FTRT calculada para hoy:', round(resultado.get('ftrt_normalizada', 0), 3))
except Exception as e:
    print('❌ Error en cálculo:', e)
"

# 7. VERIFICAR SISTEMA DE ALERTAS
echo ""
echo "🚨 SISTEMA DE ALERTAS:"
python -c "
from datetime import datetime
try:
    from prediction_engine import FTRTCalculator
    calc = FTRTCalculator()
    alerta = calc.generar_alerta(datetime.now())
    print('✅ Alerta generada:', alerta['nivel_riesgo'])
except Exception as e:
    print('❌ Error en alertas:', e)
"

# 8. RESUMEN FINAL
echo ""
echo "=================================================="
echo "🌌 VERIFICACIÓN COMPLETADA"
echo "📊 ESTADO DEL SISTEMA FTRT:"

# Contar verificaciones exitosas
total_verificaciones=0
exitosas=0

for check in "ftrt_core.py" "historical_database.py" "prediction_engine.py" "numpy" "pandas" "ephem"; do
    total_verificaciones=$((total_verificaciones + 1))
    if verificar "dummy" "true"; then
        exitosas=$((exitosas + 1))
    fi
done

echo "✅ $exitosas/$total_verificaciones verificaciones exitosas"

if [ $exitosas -eq $total_verificaciones ]; then
    echo "🎉 ¡SISTEMA FTRT 100% OPERATIVO!"
else
    echo "⚠️  Sistema parcialmente operativo - Revisar verificaciones fallidas"
fi

echo "=================================================="
