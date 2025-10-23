"""
DEMOSTRACIÓN WEB - SISTEMA FTRT INTERACTIVO
Versión simplificada para implementación web
"""

from config.global_variables import *
import json

class FTRTWebDemo:
    def __init__(self):
        self.datos_demo = {
            'configuraciones': {
                '2003_halloween': {'ftrt': 4.878, 'alerta': 'EXTREMO', 'color': '💜'},
                '2024_mayo': {'ftrt': 2.943, 'alerta': 'CRITICO', 'color': '🔴'},
                '2025_q4': {'ftrt': 3.215, 'alerta': 'CRITICO', 'color': '🔴'},
                '2035_gran_alineacion': {'ftrt': 5.161, 'alerta': 'EXTREMO', 'color': '💜'}
            },
            'correlaciones': CORRELACIONES_FTRT,
            'predicciones': PREDICCIONES_FUTURAS,
            'validacion': VALIDACION_AMAZON_2025
        }
    
    def generar_json_datos(self):
        """Genera datos en formato JSON para uso web"""
        return json.dumps(self.datos_demo, indent=2, ensure_ascii=False)
    
    def generar_reporte_web(self):
        """Genera reporte optimizado para web"""
        reporte = {
            'titulo': 'SISTEMA FTRT - ANÁLISIS INTERACTIVO',
            'resumen': {
                'precision_modelo': f"{VALIDACION_AMAZON_2025['precision']}%",
                'eventos_analizados': len(EVENTOS_HISTORICOS),
                'predicciones_futuras': len(PREDICCIONES_FUTURAS)
            },
            'configuraciones': self.datos_demo['configuraciones'],
            'alertas_activas': [
                {'fecha': '2025-11-15', 'nivel': 'ELEVADO', 'riesgo': 'sistemas_financieros'},
                {'fecha': '2026-03-20', 'nivel': 'CRITICO', 'riesgo': 'evento_carrington_moderado'}
            ]
        }
        return reporte

# Ejecutar demostración web
if __name__ == "__main__":
    demo = FTRTWebDemo()
    
    print("🌐 DEMOSTRACIÓN WEB - SISTEMA FTRT")
    print("=" * 50)
    
    # Generar JSON para frontend
    json_datos = demo.generar_json_datos()
    print("📊 Datos JSON listos para frontend:")
    print(json_datos[:500] + "...")  # Mostrar solo parte inicial
    
    # Reporte web
    reporte = demo.generar_reporte_web()
    print(f"\n🎯 Reporte Web:")
    print(f"   Título: {reporte['titulo']}")
    print(f"   Precisión: {reporte['resumen']['precision_modelo']}")
    print(f"   Alertas activas: {len(reporte['alertas_activas'])}")
    
    print("\n✅ Sistema listo para integración web")
