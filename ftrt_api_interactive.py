"""
Sistema Interactivo FTRT + API
Autores: Benjamin Cabeza Duran / DeepSeek / GitHub Copilot
Fecha: Octubre 2025
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import ephem
from datetime import datetime, timedelta
import json

app = Flask(__name__)
CORS(app)

class FTRTInteractiveSystem:
    def __init__(self):
        self.initialize_system()
        
    def initialize_system(self):
        """Inicializa el sistema con configuraciones base"""
        self.load_constants()
        self.load_historical_data()
        self.initialize_visualization_engine()
    
    def load_constants(self):
        """Carga constantes del sistema"""
        self.R_SOL = 6.957e8  # Radio solar en metros
        self.PLANETARY_MASSES = {
            'mercury': 3.3011e23,
            'venus': 4.8675e24,
            'earth': 5.9722e24,
            'mars': 6.4171e23,
            'jupiter': 1.8982e27,
            'saturn': 5.6834e26,
            'uranus': 8.6810e25,
            'neptune': 1.0241e26
        }
        
        self.ALERT_LEVELS = {
            'normal': {'threshold': 0.8, 'color': '🟢'},
            'moderate': {'threshold': 1.2, 'color': '🟡'},
            'elevated': {'threshold': 1.8, 'color': '🟠'},
            'critical': {'threshold': 2.5, 'color': '🔴'},
            'extreme': {'threshold': 10.0, 'color': '💜'}
        }
    
    def load_historical_data(self):
        """Carga datos históricos de eventos solares"""
        self.historical_events = {
            'carrington': {
                'date': '1859-09-01',
                'ftrt': 3.21,
                'description': 'Evento Carrington',
                'effects': ['Auroras globales', 'Fallo telégrafos']
            },
            'halloween': {
                'date': '2003-10-29',
                'ftrt': 4.87,
                'description': 'Tormentas Halloween',
                'effects': ['Apagones', 'Interferencia satelital']
            },
            'may2024': {
                'date': '2024-05-10',
                'ftrt': 1.34,
                'description': 'Tormenta Solar Mayo 2024',
                'effects': ['GPS disruption', 'Radio blackouts']
            }
        }
    
    def initialize_visualization_engine(self):
        """Configura el motor de visualización"""
        self.plot_config = {
            'theme': 'solar',
            'colorscales': {
                'ftrt': 'Plasma',
                'energy': 'Viridis',
                'risk': 'RdYlGn_r'
            }
        }
    
    def calculate_ftrt(self, date):
        """Calcula FTRT para una fecha específica"""
        total_ftrt = 0
        contributions = {}
        
        for planet, mass in self.PLANETARY_MASSES.items():
            body = getattr(ephem, planet.capitalize())()
            body.compute(date)
            distance = body.sun_distance * 149597870700  # AU to meters
            
            ftrt = (mass * self.R_SOL) / (distance ** 3)
            contributions[planet] = ftrt
            total_ftrt += ftrt
        
        return {
            'date': date,
            'ftrt_total': total_ftrt,
            'ftrt_normalized': total_ftrt / contributions['jupiter'],
            'contributions': contributions
        }
    
    def generate_report(self, date):
        """Genera reporte completo de análisis FTRT"""
        ftrt_data = self.calculate_ftrt(date)
        alert_level = self.get_alert_level(ftrt_data['ftrt_normalized'])
        
        report = {
            'date': date,
            'ftrt': ftrt_data['ftrt_normalized'],
            'alert_level': alert_level,
            'planetary_config': self.get_planetary_config(date),
            'energy_levels': self.calculate_energy_levels(ftrt_data),
            'recommendations': self.generate_recommendations(alert_level)
        }
        
        return report
    
    def get_alert_level(self, ftrt):
        """Determina nivel de alerta basado en FTRT"""
        for level, info in self.ALERT_LEVELS.items():
            if ftrt <= info['threshold']:
                return {'level': level, 'color': info['color']}
        return {'level': 'extreme', 'color': '💜'}
    
    def get_planetary_config(self, date):
        """Obtiene configuración planetaria para fecha"""
        config = {}
        zodiac = ['Aries', 'Tauro', 'Géminis', 'Cáncer', 'Leo', 'Virgo', 
                  'Libra', 'Escorpio', 'Sagitario', 'Capricornio', 'Acuario', 'Piscis']
        
        for planet in self.PLANETARY_MASSES.keys():
            body = getattr(ephem, planet.capitalize())()
            body.compute(date)
            
            long_deg = np.degrees(body.hlong)
            zodiac_sign = zodiac[int(long_deg / 30)]
            
            config[planet] = {
                'longitude': long_deg,
                'constellation': zodiac_sign,
                'distance': body.sun_distance
            }
        
        return config
    
    def calculate_energy_levels(self, ftrt_data):
        """Calcula niveles de energía basados en FTRT"""
        base_ftrt = ftrt_data['ftrt_normalized']
        
        return {
            'transformation': min(100, base_ftrt * 20),
            'intensity': min(100, base_ftrt * 18),
            'revelation': min(100, base_ftrt * 22),
            'integration': min(100, base_ftrt * 15)
        }
    
    def generate_recommendations(self, alert_level):
        """Genera recomendaciones basadas en nivel de alerta"""
        recommendations = {
            'normal': ['Monitoreo regular', 'Mantener protocolos estándar'],
            'moderate': ['Aumentar frecuencia de monitoreo', 'Revisar protecciones'],
            'elevated': ['Activar protocolos de protección', 'Preparar sistemas backup'],
            'critical': ['Implementar medidas máximas', 'Posible evacuación'],
            'extreme': ['Activar protocolo Carrington', 'Protección total requerida']
        }
        
        return recommendations.get(alert_level['level'], ['Error: Nivel no reconocido'])

# API Routes
@app.route('/api/ftrt/calculate', methods=['POST'])
def calculate_ftrt_endpoint():
    """API endpoint para cálculo FTRT"""
    data = request.get_json()
    date = data.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    system = FTRTInteractiveSystem()
    result = system.calculate_ftrt(date)
    
    return jsonify(result)

@app.route('/api/ftrt/report', methods=['POST'])
def generate_report_endpoint():
    """API endpoint para generar reporte completo"""
    data = request.get_json()
    date = data.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    system = FTRTInteractiveSystem()
    report = system.generate_report(date)
    
    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True, port=5000)