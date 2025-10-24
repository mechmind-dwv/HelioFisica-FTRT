"""
Tests para el Sistema de Logging FTRT
"""

import unittest
from datetime import datetime
import os
import json
import shutil
from utils.logger import FTRTLogger

class TestFTRTLogger(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.logger = FTRTLogger(nombre="test_ftrt", nivel="DEBUG")
        self.log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    
    def tearDown(self):
        """Limpieza después de cada test"""
        if os.path.exists(self.log_dir):
            shutil.rmtree(self.log_dir)
    
    def test_crear_logger(self):
        """Test creación básica del logger"""
        self.assertIsNotNone(self.logger)
        self.assertTrue(os.path.exists(self.log_dir))
    
    def test_log_calculo_ftrt(self):
        """Test registro de cálculo FTRT"""
        fecha = datetime.now()
        resultado = {'ftrt_normalizada': 1.5}
        duracion = 0.45
        
        self.logger.log_calculo_ftrt(fecha, resultado, duracion)
        
        # Verificar archivo de métricas
        metricas_file = os.path.join(self.log_dir, 'metricas.json')
        self.assertTrue(os.path.exists(metricas_file))
        
        with open(metricas_file, 'r') as f:
            metricas = json.load(f)
        
        self.assertIn('calculos', metricas)
        self.assertEqual(len(metricas['calculos']), 1)
        self.assertEqual(metricas['calculos'][0]['ftrt'], 1.5)
    
    def test_log_prediccion(self):
        """Test registro de predicción"""
        fecha = datetime.now()
        self.logger.log_prediccion(fecha, 2.1, 0.95)
        
        metricas_file = os.path.join(self.log_dir, 'metricas.json')
        with open(metricas_file, 'r') as f:
            metricas = json.load(f)
        
        self.assertIn('predicciones', metricas)
        self.assertEqual(len(metricas['predicciones']), 1)
        self.assertEqual(metricas['predicciones'][0]['ftrt'], 2.1)
    
    def test_log_alerta(self):
        """Test registro de alerta"""
        alerta = {
            'nivel_riesgo': 'CRÍTICO',
            'color_alerta': '🔴',
            'ftrt_normalizada': 2.5
        }
        
        self.logger.log_alerta(alerta)
        
        metricas_file = os.path.join(self.log_dir, 'metricas.json')
        with open(metricas_file, 'r') as f:
            metricas = json.load(f)
        
        self.assertIn('alertas', metricas)
        self.assertEqual(len(metricas['alertas']), 1)
        self.assertEqual(metricas['alertas'][0]['ftrt'], 2.5)
    
    def test_niveles_log(self):
        """Test diferentes niveles de log"""
        # Test todos los niveles
        self.logger.debug("Test debug")
        self.logger.info("Test info")
        self.logger.warning("Test warning")
        self.logger.error("Test error")
        self.logger.critical("Test critical")
        
        # Verificar archivo de log
        log_file = os.path.join(self.log_dir, 'ftrt.log')
        self.assertTrue(os.path.exists(log_file))
        
        with open(log_file, 'r') as f:
            contenido = f.read()
            self.assertIn("Test debug", contenido)
            self.assertIn("Test critical", contenido)
    
    def test_rotacion_archivos(self):
        """Test rotación de archivos de log"""
        # Generar suficientes logs para forzar rotación
        for i in range(1000):
            self.logger.info(f"Test log {i}" * 100)  # Mensaje grande
        
        # Verificar que existen archivos de backup
        archivos = os.listdir(self.log_dir)
        archivos_log = [f for f in archivos if f.startswith('ftrt.log')]
        self.assertGreater(len(archivos_log), 1)
    
    def test_eventos_criticos(self):
        """Test log de eventos críticos"""
        # Generar eventos críticos
        for i in range(5):
            self.logger.critical(f"Evento crítico {i}")
        
        # Verificar archivo de eventos críticos
        eventos_file = os.path.join(self.log_dir, 'eventos_criticos.log')
        self.assertTrue(os.path.exists(eventos_file))
        
        with open(eventos_file, 'r') as f:
            contenido = f.read()
            self.assertEqual(contenido.count("Evento crítico"), 5)

if __name__ == '__main__':
    unittest.main()