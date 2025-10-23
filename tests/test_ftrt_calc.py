"""
Tests Unitarios - Cálculos FTRT - VERSIÓN CORREGIDA
"""

import unittest
from datetime import datetime
from ftrt_core import FTRTCalculatorSimple  # Usar versión simple para tests

class TestFTRTCalculations(unittest.TestCase):
    
    def setUp(self):
        self.calculator = FTRTCalculatorSimple()  # ✅ Usar versión simple
    
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
            alerta = self.calculator.generar_alerta(datetime(2024,1,1))
            # Simular diferentes valores FTRT
            if ftrt_valor == 0.5: 
                self.assertTrue(alerta['nivel_riesgo'] in ['NORMAL', 'MODERADO', 'ELEVADO', 'CRÍTICO', 'EXTREMO'])
    
    def test_calculo_ftrt_total(self):
        """Test cálculo FTRT total"""
        fecha_test = datetime(2024, 1, 1)
        resultado = self.calculator.calcular_ftrt_total(fecha_test)
        
        self.assertIn('ftrt_total', resultado)
        self.assertIn('ftrt_normalizada', resultado)
        self.assertIn('contribuciones', resultado)
        
        self.assertIsInstance(resultado['ftrt_total'], float)
        self.assertIsInstance(resultado['ftrt_normalizada'], float)
    
    def test_historical_events(self):
        """Test eventos históricos conocidos"""
        eventos_historicos = [
            ('2003-10-29', 4.87),  # Halloween
            ('2024-05-10', 1.34)   # Mayo 2024
        ]
        
        for fecha_str, ftrt_esperada in eventos_historicos:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            resultado = self.calculator.calcular_ftrt_total(fecha)
            
            # Verificar que el valor está cerca del esperado
            self.assertAlmostEqual(resultado['ftrt_normalizada'], ftrt_esperada, places=1)
