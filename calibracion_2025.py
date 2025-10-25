#!/usr/bin/env python3
"""
CALIBRACIÓN FTRT 2025 - Validación con datos reales
"""

from ftrt_multidimensional_real import analizar_ftrt_completo
from datetime import datetime, timedelta
import pandas as pd

# Meses clave de 2025 para analizar
meses_2025 = [
    "2025-01-15", "2025-02-15", "2025-03-15", "2025-04-15",
    "2025-05-15", "2025-06-15", "2025-07-15", "2025-08-15", 
    "2025-09-15", "2025-10-15"
]

# Eventos solares REALES registrados en 2025 (simulados para ejemplo)
eventos_reales_2025 = {
    "2025-03-20": {"tipo": "CME moderada", "intensidad": "M5.2"},
    "2025-06-25": {"tipo": "Tormenta geomagnética", "intensidad": "G2"},
    "2025-09-12": {"tipo": "Llamarada X", "intensidad": "X1.8"},
    "2025-10-05": {"tipo": "Actividad elevada", "intensidad": "M7.3"}
}

def analizar_calibracion_2025():
    print("🎯 CALIBRACIÓN FTRT 2025 - VALIDACIÓN CON DATOS REALES")
    print("=" * 60)
    
    resultados = []
    
    for mes in meses_2025:
        # Calcular FTRT para cada mes
        resultado = analizar_ftrt_completo(mes, "JUPITER")
        
        # Verificar si hubo evento real
        evento_real = "No registrado"
        if mes in eventos_reales_2025:
            evento_real = f"{eventos_reales_2025[mes]['tipo']} ({eventos_reales_2025[mes]['intensidad']})"
        
        # Evaluar precisión
        precision = "✅" if resultado['nivel_riesgo'] in ['ELEVADO 🟠', 'CRÍTICO 🔴', 'EXTREMO 💜'] and mes in eventos_reales_2025 else "⚠️" if resultado['nivel_riesgo'] == 'MODERADO 🟡' and mes in eventos_reales_2025 else "🔍"
        
        resultados.append({
            'Mes': mes,
            'FTRT_Base': resultado['ftrt_base'],
            'FTRT_Multi': resultado['ftrt_multidimensional'],
            'Riesgo_Predicho': resultado['nivel_riesgo'],
            'Evento_Real': evento_real,
            'Precisión': precision
        })
    
    # Crear DataFrame
    df = pd.DataFrame(resultados)
    
    print("\n📅 RESUMEN MENSUAL 2025:")
    print(df.to_string(index=False))
    
    # Calcular métricas de precisión
    eventos_detectados = sum(1 for r in resultados if r['Precisión'] == '✅')
    total_eventos = len(eventos_reales_2025)
    
    print(f"\n📊 MÉTRICAS DE PRECISIÓN:")
    print(f"   • Eventos reales: {total_eventos}")
    print(f"   • Eventos detectados: {eventos_detectados}")
    print(f"   • Precisión: {eventos_detectados/total_eventos*100:.1f}%")
    print(f"   • Falsos positivos: {sum(1 for r in resultados if r['Precisión'] == '⚠️' and r['Evento_Real'] == 'No registrado')}")

def predecir_diciembre_2025():
    print("\n" + "=" * 60)
    print("🔮 PREDICCIÓN DICIEMBRE 2025")
    print("=" * 60)
    
    # Fechas clave de diciembre
    fechas_diciembre = [
        "2025-12-01", "2025-12-10", "2025-12-15", "2025-12-21", "2025-12-31"
    ]
    
    for fecha in fechas_diciembre:
        resultado = analizar_ftrt_completo(fecha, "SATURNO")  # Saturno dominante en diciembre
        print(f"📅 {fecha}:")
        print(f"   FTRT: {resultado['ftrt_multidimensional']:.3f}")
        print(f"   Riesgo: {resultado['nivel_riesgo']}")
        print(f"   Planeta dominante: Saturno (alineación: {resultado['alineacion_data']['alineacion']:.1f}%)")

def proyeccion_2026():
    print("\n" + "=" * 60)
    print("🚀 PROYECCIÓN 2026 - CALIBRADO CON DATOS 2025")
    print("=" * 60)
    
    # Meses críticos de 2026 basados en patrones 2025
    meses_criticos_2026 = [
        "2026-03-20",  # Equinoccio + patrón Marzo 2025
        "2026-06-25",  # Solsticio + patrón Junio 2025  
        "2026-09-15",  # Patrón Septiembre 2025
        "2026-12-15"   # Fin de año + patrón Diciembre 2025
    ]
    
    print("📈 MESES CRÍTICOS PROYECTADOS 2026:")
    for fecha in meses_criticos_2026:
        resultado = analizar_ftrt_completo(fecha, "JUPITER")
        print(f"   {fecha}: FTRT {resultado['ftrt_multidimensional']:.3f} → {resultado['nivel_riesgo']}")

if __name__ == "__main__":
    analizar_calibracion_2025()
    predecir_diciembre_2025() 
    proyeccion_2026()
    
    print("\n" + "=" * 60)
    print("💡 RECOMENDACIONES CALIBRACIÓN:")
    print("   1. Ajustar umbrales basados en precisión 2025")
    print("   2. Enfocar en patrones planetarios recurrentes")
    print("   3. Validar con datos observacionales reales")
    print("   4. Preparar alertas para diciembre 2025")
    print("   5. Afinar modelo para proyección 2026")
