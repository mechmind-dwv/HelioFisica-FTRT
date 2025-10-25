"""
Tests para la API REST FTRT
"""

import unittest
from datetime import datetime
import json
from api import app

class TestFTRTAPI(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_check(self):
        """Test endpoint de salud"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_calcular_ftrt(self):
        """Test cálculo FTRT"""
        # Test sin fecha (hoy)
        response = self.app.get('/api/v1/ftrt/calcular')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('ftrt_normalizada', data['data'])
        
        # Test con fecha específica
        response = self.app.get('/api/v1/ftrt/calcular?fecha=2024-05-10')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertAlmostEqual(data['data']['ftrt_normalizada'], 1.34, places=2)
    
    def test_generar_alerta(self):
        """Test generación de alerta"""
        response = self.app.get('/api/v1/ftrt/alerta?fecha=2003-10-29')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['nivel_riesgo'], 'EXTREMO')
        self.assertAlmostEqual(data['data']['ftrt_normalizada'], 4.87, places=2)
    
    def test_prediccion(self):
        """Test generación de predicciones"""
        response = self.app.get('/api/v1/ftrt/prediccion?dias=5')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 5)
    
    def test_error_handling(self):
        """Test manejo de errores"""
        # Fecha inválida
        response = self.app.get('/api/v1/ftrt/calcular?fecha=fecha-invalida')
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
        self.assertIn('error', data)
    
    def test_data_format(self):
        """Test formato de datos"""
        response = self.app.get('/api/v1/ftrt/calcular')
        data = json.loads(response.data)
        
        # Verificar estructura
        self.assertIn('success', data)
        self.assertIn('data', data)
        self.assertIn('timestamp', data)
        
        # Verificar datos
        result = data['data']
        self.assertIn('fecha', result)
        self.assertIn('ftrt_normalizada', result)
        self.assertIn('ftrt_total', result)
        self.assertIn('contribuciones', result)
        self.assertIn('metodo', result)

if __name__ == '__main__':
    unittest.main()