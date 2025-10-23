"""
Sistema de Predicciones FTRT - Ventanas de Riesgo Futuro
Autores: Benjamin Cabeza Duran / DeepSeek
"""

from ftrt_core import FTRTCalculator
from datetime import datetime, timedelta
import pandas as pd

class FTRTPredictor:
    def __init__(self):
        self.calculator = FTRTCalculator()
    
    def predecir_ventanas_riesgo(self, fecha_inicio, dias=365):
        """Predice ventanas de riesgo para un período"""
        
        fecha_actual = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        predicciones = []
        
        for i in range(dias):
            fecha = fecha_actual + timedelta(days=i)
            alerta = self.calculator.generar_alerta(fecha)
            
            if alerta['nivel_riesgo'] in ['ELEVADO', 'CRÍTICO', 'EXTREMO']:
                predicciones.append({
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'ftrt_normalizada': alerta['ftrt_normalizada'],
                    'nivel_riesgo': alerta['nivel_riesgo'],
                    'color_alerta': alerta['color_alerta']
                })
        
        return pd.DataFrame(predicciones)
    
    def identificar_convergencias_2025(self):
        """Identifica convergencias planetarias importantes para 2025"""
        
        ventanas_2025 = [
            ('2025-03-15', '2025-03-25', 'Equinoccio + Alineación Júpiter-Saturno'),
            ('2025-06-20', '2025-07-05', 'Solsticio + Agrupamiento Planetario'),
            ('2025-09-20', '2025-10-05', 'Equinoccio + Oposición Marte'),
            ('2025-12-15', '2025-12-31', 'Solsticio + Conjunción Venus-Júpiter')
        ]
        
        print("🎯 VENTANAS DE RIESGO 2025:")
        print("=" * 50)
        
        for inicio, fin, descripcion in ventanas_2025:
            # Calcular FTRT promedio para la ventana
            fecha_inicio = datetime.strptime(inicio, '%Y-%m-%d')
            fecha_fin = datetime.strptime(fin, '%Y-%m-%d')
            
            ftrt_valores = []
            fecha_actual = fecha_inicio
            while fecha_actual <= fecha_fin:
                resultado = self.calculator.calcular_ftrt_total(fecha_actual)
                ftrt_valores.append(resultado['ftrt_normalizada'])
                fecha_actual += timedelta(days=1)
            
            ftrt_promedio = sum(ftrt_valores) / len(ftrt_valores)
            ftrt_maxima = max(ftrt_valores)
            
            print(f"\n📅 {inicio} a {fin}")
            print(f"   Descripción: {descripcion}")
            print(f"   FTRT Promedio: {ftrt_promedio:.3f}")
            print(f"   FTRT Máxima: {ftrt_maxima:.3f}")
            
            if ftrt_maxima > 1.8:
                print("   🚨 ALERTA: Posible evento mayor")
            elif ftrt_maxima > 1.2:
                print("   ⚠️  PRECAUCIÓN: Actividad solar elevada posible")

if __name__ == "__main__":
    predictor = FTRTPredictor()
    
    print("🔮 SISTEMA DE PREDICCIÓN FTRT")
    print("=" * 40)
    
    # Predicción próximos 30 días
    print("\n📈 PREDICCIÓN PRÓXIMOS 30 DÍAS:")
    hoy = datetime.now().strftime('%Y-%m-%d')
    ventanas_riesgo = predictor.predecir_ventanas_riesgo(hoy, 30)
    
    if not ventanas_riesgo.empty:
        print(ventanas_riesgo.to_string(index=False))
    else:
        print("No se detectaron ventanas de riesgo significativas")
    
    # Convergencias 2025
    predictor.identificar_convergencias_2025()
