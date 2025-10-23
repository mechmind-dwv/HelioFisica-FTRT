"""
Tests de Correlaciones Estadísticas
Autores: Benjamin Cabeza Duran / DeepSeek
"""

import unittest
import json
import pandas as pd
from historical_database import generate_historical_correlations

class TestCorrelations(unittest.TestCase):
    
    def test_correlations_structure(self):
        """Test estructura de correlaciones"""
        
        correlations = generate_historical_correlations()
        
        self.assertIsInstance(correlations, list)
        self.assertGreater(len(correlations), 0)
        
        for correlation in correlations:
            self.assertIn('correlation_type', correlation)
            self.assertIn('r_value', correlation)
            self.assertIn('p_value', correlation)
            self.assertIn('sample_size', correlation)
    
    def test_correlation_significance(self):
        """Test significancia estadística de correlaciones"""
        
        correlations = generate_historical_correlations()
        
        for correlation in correlations:
            # Verificar que p-value indica significancia
            self.assertLess(correlation['p_value'], 0.05)
            
            # Verificar que el tamaño de muestra es adecuado
            self.assertGreater(correlation['sample_size'], 30)
    
    def test_ftrt_storm_correlation(self):
        """Test correlación específica FTRT vs tormentas"""
        
        correlations = generate_historical_correlations()
        ftft_storm_corr = next(
            (c for c in correlations if c['correlation_type'] == 'FTRT vs Storm Magnitude'), 
            None
        )
        
        self.assertIsNotNone(ftft_storm_corr)
        self.assertGreater(ftft_storm_corr['r_value'], 0.7)  # Correlación fuerte
    
    def test_prediction_accuracy(self):
        """Test precisión predictiva del modelo"""
        
        # Cargar métricas de correlaciones.json
        with open('data/correlations.json', 'r') as f:
            data = json.load(f)
        
        accuracy = data['predictive_metrics']['accuracy_ftrt_gt_1_5']
        self.assertGreater(accuracy, 0.8)  # Precisión > 80%

if __name__ == '__main__':
    unittest.main()
