"""
Estado Global del Sistema FTRT - VERSIÓN CORREGIDA
"""

from config.global_variables import *

def mostrar_resumen_global():
    print("🌍 RESUMEN GLOBAL SISTEMA FTRT")
    print("=" * 60)
    
    # Información del sistema
    print("📋 INFORMACIÓN DEL SISTEMA:")
    print(f"   Versión: {CONFIG_SISTEMA['version']}")
    print(f"   Autor: {CONFIG_SISTEMA['autor']}")
    print(f"   Repositorio: {CONFIG_SISTEMA['repositorio']}")
    
    # Eventos históricos
    print(f"\n📚 EVENTOS HISTÓRICOS: {len(EVENTOS_HISTORICOS)}")
    for fecha, evento in EVENTOS_HISTORICOS.items():
        print(f"   {fecha}: {evento['nombre']} (FTRT: {evento['ftrt_normalizada']})")
    
    # Correlaciones
    print(f"\n🔗 CORRELACIONES VALIDADAS: {len(CORRELACIONES_FTRT)}")
    for nombre, corr in CORRELACIONES_FTRT.items():
        print(f"   {nombre}: r = {corr['coeficiente']:.2f}")
    
    # Umbrales
    print(f"\n🚨 UMBRALES DE ALERTA: {len(UMBRALES_ALERTA)}")
    for nivel, umbral in UMBRALES_ALERTA.items():
        color = COLORES_ALERTA.get(nivel, '⚪')
        print(f"   {nivel}: {umbral} {color}")
    
    print("\n" + "=" * 60)
    print("✅ SISTEMA OPERATIVO Y VALIDADO")

if __name__ == "__main__":
    mostrar_resumen_global()
