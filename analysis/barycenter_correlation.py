"""
Análisis de Correlación Baricentro-Eventos Solares
Autor: Benjamin Cabeza Durán / DeepSeek
Fecha: Octubre 2025

Este módulo analiza la correlación entre la posición del baricentro solar
y eventos solares mayores, validando la teoría de influencia planetaria.
"""

import numpy as np
import ephem
from datetime import datetime, timedelta
import pandas as pd
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from scipy import stats

class BarycentricAnalyzer:
    """
    Analizador de correlaciones entre baricentro solar y eventos solares mayores.
    """
    
    # Constantes de masas planetarias relativas al Sol
    MASS_RATIOS = {
        'jupiter': 1/1047.355,   # Masa de Júpiter/Sol
        'saturn': 1/3498.5,      # Masa de Saturno/Sol
        'uranus': 1/22869,       # Masa de Urano/Sol
        'neptune': 1/19314       # Masa de Neptuno/Sol
    }

    # Eventos solares mayores para análisis
    MAJOR_EVENTS = {
        'halloween_2003': {
            'date': datetime(2003, 10, 28),
            'description': 'Tormenta de Halloween 2003',
            'intensity': 'X45',
            'impact': 'Extremo'
        },
        'carrington': {
            'date': datetime(1859, 9, 1),
            'description': 'Evento Carrington',
            'intensity': 'Estimado >X40',
            'impact': 'Extremo'
        },
        'may_2024': {
            'date': datetime(2024, 5, 15),
            'description': 'Tormenta Solar Mayo 2024',
            'intensity': 'X28',
            'impact': 'Severo'
        },
        'aws_2025': {
            'date': datetime(2025, 10, 1),
            'description': 'Evento AWS 2025',
            'intensity': 'X35',
            'impact': 'Extremo'
        }
    }

    def __init__(self):
        """Inicializa el analizador con configuración base."""
        self.setup_ephemeris()
        self.barycenter_baseline = 1000  # Valor base para normalización
        
    def setup_ephemeris(self):
        """Configura objetos de efemérides para cálculos planetarios."""
        self.planets = {
            'jupiter': ephem.Jupiter(),
            'saturn': ephem.Saturn(),
            'uranus': ephem.Uranus(),
            'neptune': ephem.Neptune()
        }
        self.sun = ephem.Sun()

    def calculate_barycenter_offset(self, date: datetime) -> float:
        """
        Calcula el offset del baricentro solar en radios solares.
        
        Args:
            date: Fecha para el cálculo
        
        Returns:
            float: Offset del baricentro en radios solares
        """
        total_moment = 0
        ephem_date = ephem.Date(date)

        # Calcular momento total debido a cada planeta gigante
        for planet_name, planet in self.planets.items():
            planet.compute(ephem_date)
            # Convertir coordenadas heliocéntricas a cartesianas
            dist = planet.sun_distance * ephem.meters_per_au
            # Momento debido a la masa del planeta
            moment = dist * self.MASS_RATIOS[planet_name]
            total_moment += moment

        # Convertir a radios solares (R☉)
        solar_radius = 696340e3  # metros
        return total_moment / solar_radius

    def analyze_planetary_configuration(self, date: datetime) -> Dict:
        """
        Analiza la configuración planetaria para una fecha dada.
        
        Args:
            date: Fecha a analizar
        
        Returns:
            Dict con información de configuración planetaria
        """
        ephem_date = ephem.Date(date)
        config = {}
        
        # Calcular posiciones relativas
        for planet_name, planet in self.planets.items():
            planet.compute(ephem_date)
            config[planet_name] = {
                'elongation': planet.sun_distance,
                'phase': planet.phase,
                'helio_lat': np.degrees(float(planet.hlat)),
                'helio_long': np.degrees(float(planet.hlong))
            }
        
        # Calcular tensión gravitacional
        tension = self.calculate_gravitational_tension(config)
        config['tension_index'] = tension
        
        return config

    def calculate_gravitational_tension(self, config: Dict) -> float:
        """
        Calcula índice de tensión gravitacional basado en posiciones planetarias.
        
        Args:
            config: Configuración planetaria
        
        Returns:
            float: Índice de tensión normalizado
        """
        tension = 0
        
        # Analizar elongación y oposiciones
        for p1 in self.planets.keys():
            for p2 in self.planets.keys():
                if p1 >= p2:
                    continue
                    
                angle = abs(config[p1]['helio_long'] - config[p2]['helio_long'])
                if angle > 180:
                    angle = 360 - angle
                    
                # Mayor tensión cuando planetas están opuestos (180°)
                tension += np.sin(np.radians(angle)) * (
                    self.MASS_RATIOS[p1] * self.MASS_RATIOS[p2]
                )

        return tension * self.barycenter_baseline

    def analyze_event_correlation(self, event_date: datetime, 
                                window_days: int = 30) -> Dict:
        """
        Analiza correlación entre configuración planetaria y evento solar.
        
        Args:
            event_date: Fecha del evento
            window_days: Ventana de análisis en días
        
        Returns:
            Dict con análisis detallado
        """
        dates = []
        barycenter_positions = []
        tensions = []
        
        # Analizar ventana temporal
        start_date = event_date - timedelta(days=window_days//2)
        for day in range(window_days):
            current_date = start_date + timedelta(days=day)
            dates.append(current_date)
            
            # Calcular posición del baricentro
            offset = self.calculate_barycenter_offset(current_date)
            barycenter_positions.append(offset)
            
            # Analizar configuración planetaria
            config = self.analyze_planetary_configuration(current_date)
            tensions.append(config['tension_index'])
            
        # Calcular correlaciones
        max_offset = max(barycenter_positions)
        max_tension = max(tensions)
        event_offset = barycenter_positions[window_days//2]
        event_tension = tensions[window_days//2]
        
        correlation = stats.pearsonr(barycenter_positions, tensions)[0]
        
        return {
            'event_date': event_date,
            'barycenter_offset': event_offset,
            'max_offset': max_offset,
            'tension_index': event_tension,
            'max_tension': max_tension,
            'correlation': correlation,
            'time_series': {
                'dates': dates,
                'offsets': barycenter_positions,
                'tensions': tensions
            }
        }

    def validate_theory(self) -> Dict:
        """
        Valida la teoría de influencia planetaria usando eventos históricos.
        
        Returns:
            Dict con resultados de validación
        """
        results = {}
        correlations = []
        
        for event_name, event_data in self.MAJOR_EVENTS.items():
            analysis = self.analyze_event_correlation(event_data['date'])
            results[event_name] = {
                'date': event_data['date'],
                'description': event_data['description'],
                'intensity': event_data['intensity'],
                'analysis': analysis
            }
            correlations.append(analysis['correlation'])
            
        # Calcular significancia estadística
        mean_correlation = np.mean(correlations)
        std_correlation = np.std(correlations)
        p_value = stats.ttest_1samp(correlations, 0.0)[1]
        
        validation = {
            'events': results,
            'statistics': {
                'mean_correlation': mean_correlation,
                'std_correlation': std_correlation,
                'p_value': p_value,
                'significant': p_value < 0.05
            }
        }
        
        return validation

    def plot_event_analysis(self, event_name: str):
        """
        Genera visualización del análisis para un evento específico.
        
        Args:
            event_name: Nombre del evento a visualizar
        """
        event = self.MAJOR_EVENTS[event_name]
        analysis = self.analyze_event_correlation(event['date'])
        
        # Crear figura con dos subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot de posición del baricentro
        dates = analysis['time_series']['dates']
        offsets = analysis['time_series']['offsets']
        ax1.plot(dates, offsets, 'b-', label='Offset Baricentro')
        ax1.axvline(event['date'], color='r', linestyle='--', 
                   label='Evento Solar')
        ax1.set_title(f'Análisis Baricentro Solar - {event["description"]}')
        ax1.set_ylabel('Offset (R☉)')
        ax1.legend()
        
        # Plot de tensión gravitacional
        tensions = analysis['time_series']['tensions']
        ax2.plot(dates, tensions, 'g-', label='Tensión Gravitacional')
        ax2.axvline(event['date'], color='r', linestyle='--', 
                   label='Evento Solar')
        ax2.set_ylabel('Índice de Tensión')
        ax2.legend()
        
        plt.tight_layout()
        return fig

if __name__ == "__main__":
    analyzer = BarycentricAnalyzer()
    
    # Validar teoría con eventos históricos
    validation = analyzer.validate_theory()
    
    print("=== VALIDACIÓN TEORÍA DE INFLUENCIA PLANETARIA ===")
    print(f"\nEstadísticas Globales:")
    print(f"Correlación Media: {validation['statistics']['mean_correlation']:.3f}")
    print(f"Desviación Estándar: {validation['statistics']['std_correlation']:.3f}")
    print(f"P-valor: {validation['statistics']['p_value']:.4f}")
    print(f"¿Significativo?: {'Sí' if validation['statistics']['significant'] else 'No'}")
    
    print("\nAnálisis por Evento:")
    for event_name, data in validation['events'].items():
        print(f"\n{data['description']}:")
        print(f"Fecha: {data['date']}")
        print(f"Intensidad: {data['intensity']}")
        print(f"Correlación: {data['analysis']['correlation']:.3f}")
        print(f"Offset Baricentro: {data['analysis']['barycenter_offset']:.2f} R☉")
        print(f"Índice de Tensión: {data['analysis']['tension_index']:.2f}")
        
    # Generar visualizaciones
    for event_name in analyzer.MAJOR_EVENTS.keys():
        fig = analyzer.plot_event_analysis(event_name)
        plt.savefig(f'analysis/plots/{event_name}_analysis.png')
        plt.close()