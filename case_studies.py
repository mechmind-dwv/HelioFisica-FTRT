"""
Análisis de Casos de Estudio: Halloween 2003 y Mayo 2024
Autores: Benjamin Cabeza Duran / DeepSeek
"""

import datetime
import pandas as pd
import matplotlib.pyplot as plt
from ftrt_core import FTRTCalculator

class CaseStudyAnalyzer:
    def __init__(self):
        self.calculator = FTRTCalculator()
    
    def analyze_halloween_2003(self):
        """Análisis detallado tormenta Halloween 2003"""
        
        dates_2003 = [
            '2003-10-26', '2003-10-27', '2003-10-28', 
            '2003-10-29', '2003-10-30', '2003-11-04'
        ]
        
        results = []
        for date_str in dates_2003:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            result = self.calculator.calcular_ftrt_total(date)
            results.append(result)
        
        df_2003 = pd.DataFrame(results)
        
        print("=== TORMENTA HALLOWEEN 2003 ===")
        print(f"FTRT Máxima: {df_2003['ftrt_normalizada'].max():.3f} (29 Oct)")
        print(f"Configuración: Tierra-Venus-Júpiter en cuadratura")
        
        return df_2003
    
    def analyze_may_2024_storm(self):
        """Análisis tormenta solar Mayo 2024"""
        
        dates_2024 = [
            '2024-05-08', '2024-05-09', '2024-05-10',
            '2024-05-11', '2024-05-12', '2024-05-15'
        ]
        
        results = []
        for date_str in dates_2024:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            result = self.calculator.calcular_ftrt_total(date)
            results.append(result)
        
        df_2024 = pd.DataFrame(results)
        
        print("=== TORMENTA MAYO 2024 ===")
        print(f"FTRT Máxima: {df_2024['ftrt_normalizada'].max():.3f} (10 May)")
        print(f"Configuración: Desfile 6 planetas < 90°")
        
        return df_2024
    
    def comparative_analysis(self):
        """Análisis comparativo entre eventos"""
        
        df_2003 = self.analyze_halloween_2003()
        df_2024 = self.analyze_may_2024_storm()
        
        comparison = {
            'evento': ['Halloween 2003', 'Mayo 2024'],
            'ftrt_maxima': [
                df_2003['ftrt_normalizada'].max(),
                df_2024['ftrt_normalizada'].max()
            ],
            'duracion_dias': [10, 7],
            'llamaradas_x': [4, 14],
            'cme_velocidad_km_s': [2300, 2000]
        }
        
        return pd.DataFrame(comparison)

# Ejecución de análisis
if __name__ == "__main__":
    analyzer = CaseStudyAnalyzer()
    
    print("🔭 ANÁLISIS FTRT - CASOS DE ESTUDIO")
    print("=" * 50)
    
    df_2003 = analyzer.analyze_halloween_2003()
    df_2024 = analyzer.analyze_may_2024_storm()
    comparison = analyzer.comparative_analysis()
    
    print("\n📊 COMPARATIVA:")
    print(comparison)
