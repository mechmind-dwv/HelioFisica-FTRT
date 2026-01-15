"""
Tests Unitarios - Cálculos FTRT
Autores: Benjamin Cabeza Duran / DeepSeek
"""

import unittest
from datetime import datetime
from ftrt_core import FTRTCalculator

class TestFTRTCalculations(unittest.TestCase):
    
    def setUp(self):
        self.calculator = FTRTCalculator()
    
    def test_calculo_ftrt_individual(self):
        """Test cálculo FTRT individual para cada planeta"""
        
        fecha_test = datetime(2024, 1, 1)
        
        for planeta in self.calculator.MASAS.keys():
            ftrt = self.calculator.calcular_ftrt_individual(planeta, fecha_test)
            self.assertIsInstance(ftrt, float)
            self.assertGreaterEqual(ftrt, 0)
    
    def test_calculo_ftrt_total(self):
        """Test cálculo FTRT total"""
        
        fecha_test = datetime(2024, 1, 1)
        resultado = self.calculator.calcular_ftrt_total(fecha_test)
        
        self.assertIn('ftrt_total', resultado)
        self.assertIn('ftrt_normalizada', resultado)
        self.assertIn('contribuciones', resultado)
        
        self.assertIsInstance(resultado['ftrt_total'], float)
        self.assertIsInstance(resultado['ftrt_normalizada'], float)
        self.assertIsInstance(resultado['contribuciones'], dict)
    
    def test_alert_levels(self):
        """Test niveles de alerta"""
        
        test_cases = [
            (0.5, 'NORMAL'),
            (1.0, 'MODERADO'),
            (1.5, 'ELEVADO'),
            (2.0, 'CRÍTICO'),
            (3.0, 'EXTREMO')
        ]
        
        for ftrt_valor, nivel_esperado in test_cases:
            nivel, color = self.calculator.evaluar_riesgo(ftrt_valor)
            self.assertEqual(nivel, nivel_esperado)
    
    def test_historical_events(self):
        """Test eventos históricos conocidos"""
        
        eventos_historicos = [
            ('2003-10-29', 4.87),  # Halloween
            ('2024-05-10', 1.34)   # Mayo 2024
        ]
        
        for fecha_str, ftrt_esperada in eventos_historicos:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            resultado = self.calculator.calcular_ftrt_total(fecha)
            
            # Verificar que está dentro del 10% del valor esperado
            diferencia_porcentual = abs(resultado['ftrt_normalizada'] - ftrt_esperada) / ftrt_esperada
            self.assertLess(difference_porcentual, 0.1)

if __name__ == '__main__':
    unittest.main()
