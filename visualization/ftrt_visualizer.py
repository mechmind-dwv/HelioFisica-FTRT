"""
Visualización Interactiva FTRT
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
        
        st.title("🌠 SISTEMA INTERACTIVO FTRT")
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
                    range=[0, max(values)]
                )),
            showlegend=False,
            title="Contribuciones FTRT por Planeta"
        )
        
        st.plotly_chart(fig)
    
    def plot_energy_levels(self, energy_data):
        """Visualiza niveles de energía"""
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
        
        st.markdown(
            f"""
            <div style='padding: 20px; 
                        background-color: {colors[alert_level['level']]};
                        border-radius: 10px;
                        color: white;
                        text-align: center;
                        font-size: 24px;'>
                NIVEL DE ALERTA: {alert_level['level'].upper()} {alert_level['color']}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_recommendations(self, recommendations):
        """Muestra recomendaciones de acción"""
        st.subheader("🎯 Recomendaciones")
        for rec in recommendations:
            st.markdown(f"- {rec}")
    
    def main(self):
        """Función principal de la aplicación"""
        st.sidebar.title("🛠️ Controles")
        
        # Selector de fecha
        selected_date = st.sidebar.date_input(
            "Selecciona fecha",
            datetime.now()
        )
        
        # Obtener datos de la API
        api_url = "http://localhost:5000/api/ftrt/report"
        response = requests.post(
            api_url,
            json={'date': selected_date.strftime('%Y-%m-%d')}
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Layout principal
            col1, col2 = st.columns(2)
            
            with col1:
                self.display_alert_box(data['alert_level'])
                self.plot_ftrt_radar(data)
            
            with col2:
                self.plot_energy_levels(data['energy_levels'])
                self.plot_historical_comparison(data['ftrt'])
            
            # Recomendaciones
            self.display_recommendations(data['recommendations'])
        else:
            st.error("Error al obtener datos de la API")

if __name__ == "__main__":
    visualizer = FTRTVisualizer()
    visualizer.main()