"""
Visualización Interactiva FTRT - VERSIÓN CORREGIDA
Autores: Benjamin Cabeza Duran / DeepSeek / GitHub Copilot
Fecha: Octubre 2025
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests

class FTRTVisualizer:
    def __init__(self):
        self.setup_theme()
        self.load_color_schemes()
        
    def setup_theme(self):
        """Configura tema visual"""
        st.set_page_config(
            page_title="Sistema Interactivo FTRT",
            page_icon="🌠",
            layout="wide"
        )
        
        st.title("🌠 SISTEMA INTERACTIVO FTRT - VERSIÓN CORREGIDA")
        st.markdown("---")
    
    def load_color_schemes(self):
        """Carga esquemas de color para visualizaciones"""
        self.color_schemes = {
            'ftrt': px.colors.sequential.Plasma,
            'energy': px.colors.sequential.Viridis,
            'alert': {
                'normal': '#00ff00',
                'moderate': '#ffff00',
                'elevated': '#ffa500',
                'critical': '#ff0000',
                'extreme': '#800080'
            }
        }
    
    def plot_ftrt_radar(self, data):
        """Genera gráfico radar de contribuciones FTRT"""
        if 'contributions' not in data:
            st.warning("No hay datos de contribuciones disponibles")
            return
            
        planets = list(data['contributions'].keys())
        values = list(data['contributions'].values())
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=planets,
            fill='toself',
            name='FTRT'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(values) if values else 1]
                )),
            showlegend=False,
            title="Contribuciones FTRT por Planeta"
        )
        
        st.plotly_chart(fig)
    
    def plot_energy_levels(self, energy_data):
        """Visualiza niveles de energía"""
        if not energy_data:
            st.warning("No hay datos de niveles de energía")
            return
            
        energies = list(energy_data.keys())
        levels = list(energy_data.values())
        
        fig = go.Figure(go.Bar(
            x=energies,
            y=levels,
            marker_color=levels,
            marker_colorscale=self.color_schemes['energy']
        ))
        
        fig.update_layout(
            title="Niveles de Energía",
            yaxis_title="Porcentaje",
            xaxis_title="Tipo de Energía"
        )
        
        st.plotly_chart(fig)
    
    def plot_historical_comparison(self, current_ftrt):
        """Compara FTRT actual con eventos históricos"""
        historical = {
            'Carrington (1859)': 3.21,
            'Halloween (2003)': 4.87,
            'Mayo 2024': 1.34,
            'Actual': current_ftrt
        }
        
        events = list(historical.keys())
        values = list(historical.values())
        
        fig = go.Figure(go.Bar(
            x=events,
            y=values,
            marker_color=values,
            marker_colorscale='RdYlBu_r'
        ))
        
        fig.update_layout(
            title="Comparación con Eventos Históricos",
            yaxis_title="FTRT",
            xaxis_title="Evento"
        )
        
        st.plotly_chart(fig)
    
    def display_alert_box(self, alert_level):
        """Muestra caja de alerta estilizada"""
        colors = {
            'normal': 'green',
            'moderate': 'yellow',
            'elevated': 'orange',
            'critical': 'red',
            'extreme': 'purple'
        }
        
        alert_color = colors.get(alert_level['level'], 'gray')
        
        st.markdown(
            f"""
            <div style='padding: 20px; 
                        background-color: {alert_color};
                        border-radius: 10px;
                        color: white;
                        text-align: center;
                        font-size: 24px;'>
                🚨 NIVEL DE ALERTA: {alert_level['level'].upper()} {alert_level.get('color', '⚡')}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_recommendations(self, recommendations):
        """Muestra recomendaciones de acción"""
        st.subheader("🎯 Recomendaciones")
        for rec in recommendations:
            st.markdown(f"- {rec}")
    
    def display_fallback_data(self):
        """Muestra datos de respaldo cuando la API no está disponible"""
        st.warning("⚠️ API no disponible - Mostrando datos de ejemplo")
        
        # Datos de ejemplo
        example_data = {
            'ftrt': 2.943,
            'alert_level': {'level': 'critical', 'color': '🔴'},
            'energy_levels': {
                'transformation': 58.9,
                'intensity': 53.0,
                'revelation': 64.7,
                'integration': 44.1
            },
            'contributions': {
                'mercury': 15.8,
                'venus': 12.4,
                'earth': 9.2,
                'mars': 3.1,
                'jupiter': 28.7,
                'saturn': 18.3,
                'uranus': 8.5,
                'neptune': 4.2
            }
        }
        
        return example_data
    
    def main(self):
        """Función principal de la aplicación"""
        st.sidebar.title("🛠️ Controles")
        
        # Selector de fecha
        selected_date = st.sidebar.date_input(
            "Selecciona fecha",
            datetime.now()
        )
        
        # Obtener datos de la API en puerto 1111
        api_url = "http://localhost:1111/api/ftrt/report"
        
        try:
            response = requests.post(
                api_url,
                json={'date': selected_date.strftime('%Y-%m-%d')},
                timeout=5  # Timeout de 5 segundos
            )
            
            if response.status_code == 200:
                data = response.json()
                st.success("✅ Conectado a API FTRT")
            else:
                data = self.display_fallback_data()
                
        except requests.exceptions.ConnectionError:
            data = self.display_fallback_data()
        except requests.exceptions.Timeout:
            st.error("⏰ Timeout - La API no respondió")
            data = self.display_fallback_data()
        except Exception as e:
            st.error(f"❌ Error: {e}")
            data = self.display_fallback_data()
        
        # Layout principal
        col1, col2 = st.columns(2)
        
        with col1:
            self.display_alert_box(data['alert_level'])
            self.plot_ftrt_radar(data)
        
        with col2:
            if 'energy_levels' in data:
                self.plot_energy_levels(data['energy_levels'])
            self.plot_historical_comparison(data.get('ftrt', data.get('ftrt_total', 0)))
        
        # Mostrar datos crudos para debug
        with st.expander("🔍 Datos Crudos (Debug)"):
            st.json(data)

if __name__ == "__main__":
    visualizer = FTRTVisualizer()
    visualizer.main()
