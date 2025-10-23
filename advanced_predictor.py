"""
Sistema de Predicción Avanzado FTRT
Autores: Benjamin Cabeza Duran / DeepSeek
"""

from config.global_variables import *
from datetime import datetime, timedelta
import pandas as pd

class FTRTPredictorAvanzado:
    def __init__(self):
        self.calculos_validados = VALIDACION_AMAZON_2025
        
    def generar_reporte_predicciones(self):
        """Genera reporte completo de predicciones"""
        
        print("🔮 SISTEMA DE PREDICCIÓN FTRT AVANZADO")
        print("=" * 60)
        
        # Validación del modelo
        print("📊 VALIDACIÓN DEL MODELO:")
        val = self.calculos_validados
        print(f"   Evento Amazon 2025: FTRT Predicha {val['ftrt_predicha']} vs Real {val['ftrt_real']}")
        print(f"   Precisión: {val['precision']}%")
        print(f"   Estado: {val['validacion_cientifica']}")
        
        # Predicciones futuras
        print("\n🎯 PREDICCIONES FUTURAS VALIDADAS:")
        for fecha, pred in PREDICCIONES_FUTURAS.items():
            nivel = pred['nivel_riesgo']
            color = COLORES_ALERTA.get(nivel, '⚪')
            print(f"   {fecha}: FTRT {pred['ftrt_estimada']} | {nivel} {color}")
            print(f"      Configuración: {pred['configuracion']}")
            if 'riesgo_principal' in pred:
                print(f"      Riesgo: {pred['riesgo_principal']}")
        
        # Recomendaciones
        print("\n🛡️ RECOMENDACIONES ESTRATÉGICAS:")
        print("   • Implementar protecciones FTRT-aware en centros de datos")
        print("   • Backups distribuidos geográficamente") 
        print("   • Protocolos desconexión automática durante picos FTRT")
        print("   • Educación helio-consciente para equipos técnicos")
        
        print("\n" + "=" * 60)
        
    def analizar_ventana_riesgo(self, fecha_inicio, dias=30):
        """Analiza ventana de riesgo específica"""
        
        fecha_ini = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        riesgos = []
        
        for i in range(dias):
            fecha = fecha_ini + timedelta(days=i)
            fecha_str = fecha.strftime('%Y-%m-%d')
            
            # Verificar si hay predicción para esta fecha
            if fecha_str in PREDICCIONES_FUTURAS:
                pred = PREDICCIONES_FUTURAS[fecha_str]
                riesgos.append({
                    'fecha': fecha_str,
                    'ftrt_estimada': pred['ftrt_estimada'],
                    'nivel_riesgo': pred['nivel_riesgo'],
                    'configuracion': pred['configuracion']
                })
        
        if riesgos:
            df = pd.DataFrame(riesgos)
            print(f"\n📅 VENTANAS DE RIESGO {fecha_inicio} (+{dias} días):")
            print(df.to_string(index=False))
        else:
            print(f"\n✅ No se detectan ventanas de riesgo críticas en el período")
        
        return riesgos

def demostracion_avanzada():
    """Demostración del sistema predictivo avanzado"""
    
    predictor = FTRTPredictorAvanzado()
    
    # Reporte completo
    predictor.generar_reporte_predicciones()
    
    # Análisis de ventanas específicas
    print("\n" + "=" * 50)
    predictor.analizar_ventana_riesgo('2025-11-01', 60)  # Nov-Dic 2025
    predictor.analizar_ventana_riesgo('2026-03-01', 60)  # Mar-Abr 2026

if __name__ == "__main__":
    demostracion_avanzada()
