"""
Análisis de Casos de Estudio - Eventos Solares Históricos
Autores: Benjamin Cabeza Duran / DeepSeek
"""

import pandas as pd
import matplotlib.pyplot as plt
from ftrt_core import FTRTCalculator
from datetime import datetime, timedelta

class CaseStudyAnalyzer:
    def __init__(self):
        self.calculator = FTRTCalculator()
    
    def analizar_evento(self, fecha_evento, nombre_evento, ventana_dias=10):
        """Analiza un evento solar específico"""
        
        fecha = datetime.strptime(fecha_evento, '%Y-%m-%d')
        fecha_inicio = fecha - timedelta(days=ventana_dias//2)
        
        datos_ftrt = []
        for i in range(ventana_dias):
            fecha_actual = fecha_inicio + timedelta(days=i)
            resultado = self.calculator.calcular_ftrt_total(fecha_actual)
            datos_ftrt.append({
                'fecha': fecha_actual,
                'ftrt_normalizada': resultado['ftrt_normalizada'],
                'es_evento': fecha_actual == fecha
            })
        
        df = pd.DataFrame(datos_ftrt)
        ftrt_maxima = df['ftrt_normalizada'].max()
        ftrt_evento = df[df['es_evento']]['ftrt_normalizada'].values[0]
        
        return {
            'evento': nombre_evento,
            'fecha': fecha_evento,
            'ftrt_maxima': ftrt_maxima,
            'ftrt_evento': ftrt_evento,
            'datos': df
        }
    
    def analizar_casos_historicos(self):
        """Analiza múltiples casos históricos"""
        
        casos = [
            ('1859-09-01', 'Carrington'),
            ('1921-05-13', 'Gran Tormenta 1921'),
            ('1989-03-13', 'Apagón Quebec'),
            ('2003-10-29', 'Tormentas Halloween'),
            ('2024-05-10', 'Tormenta Mayo 2024')
        ]
        
        resultados = []
        for fecha, nombre in casos:
            analisis = self.analizar_evento(fecha, nombre)
            resultados.append(analisis)
            print(f"📈 {nombre}: FTRT = {analisis['ftrt_evento']:.3f}")
        
        return resultados
    
    def generar_reporte_comparativo(self):
        """Genera reporte comparativo de todos los casos"""
        
        resultados = self.analizar_casos_historicos()
        
        df_comparativo = pd.DataFrame([{
            'Evento': r['evento'],
            'Fecha': r['fecha'],
            'FTRT_Evento': r['ftrt_evento'],
            'FTRT_Máxima': r['ftrt_maxima'],
            'Umbral_Superado': r['ftrt_evento'] > 1.5
        } for r in resultados])
        
        print("\n📊 REPORTE COMPARATIVO:")
        print("=" * 60)
        print(df_comparativo.to_string(index=False))
        
        # Estadísticas
        eventos_sobre_umbral = df_comparativo['Umbral_Superado'].sum()
        total_eventos = len(df_comparativo)
        
        print(f"\n📈 ESTADÍSTICAS:")
        print(f"Eventos sobre umbral (FTRT > 1.5): {eventos_sobre_umbral}/{total_eventos} "
              f"({eventos_sobre_umbral/total_eventos*100:.1f}%)")
        
        return df_comparativo

if __name__ == "__main__":
    analyzer = CaseStudyAnalyzer()
    
    print("🔭 ANÁLISIS DE CASOS DE ESTUDIO FTRT")
    print("=" * 50)
    
    df_comparativo = analyzer.generar_reporte_comparativo()
