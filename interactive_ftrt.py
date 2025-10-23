"""
SISTEMA INTERACTIVO FTRT + ASTROLOGÍA INTEGRADA
Autores: Benjamin Cabeza Duran / DeepSeek
Fecha: Octubre 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from config.global_variables import *

class InteractiveFTRTAnalyzer:
    def __init__(self):
        self.configuraciones_clave = {
            '2003_halloween': {
                'fecha': '2003-10-29',
                'ftrt': 4.878,
                'planetas': {
                    'mercury': {'posicion': 'Escorpio', 'contribucion': 12.3},
                    'venus': {'posicion': 'Virgo', 'contribucion': 18.5},
                    'earth': {'posicion': 'Escorpio', 'contribucion': 8.7},
                    'mars': {'posicion': 'Piscis', 'contribucion': 2.1},
                    'jupiter': {'posicion': 'Leo', 'contribucion': 35.2},
                    'saturn': {'posicion': 'Géminis', 'contribucion': 15.8},
                    'uranus': {'posicion': 'Acuario', 'contribucion': 4.1},
                    'neptune': {'posicion': 'Acuario', 'contribucion': 3.3}
                },
                'energias': {
                    'transformacion': 95,
                    'intensidad': 92,
                    'ruptura': 88,
                    'revelacion': 85
                }
            },
            '2024_mayo': {
                'fecha': '2024-05-10', 
                'ftrt': 2.943,
                'planetas': {
                    'mercury': {'posicion': 'Tauro', 'contribucion': 15.8},
                    'venus': {'posicion': 'Aries', 'contribucion': 12.4},
                    'earth': {'posicion': 'Tauro', 'contribucion': 9.2},
                    'mars': {'posicion': 'Piscis', 'contribucion': 3.1},
                    'jupiter': {'posicion': 'Tauro', 'contribucion': 28.7},
                    'saturn': {'posicion': 'Piscis', 'contribucion': 18.3},
                    'uranus': {'posicion': 'Tauro', 'contribucion': 8.5},
                    'neptune': {'posicion': 'Piscis', 'contribucion': 4.2}
                },
                'energias': {
                    'estabilidad': 65,
                    'expresion': 72, 
                    'innovacion': 78,
                    'intuicion': 70
                }
            },
            '2025_q4': {
                'fecha': '2025-10-21',
                'ftrt': 3.215,
                'planetas': {
                    'mercury': {'posicion': 'Escorpio', 'contribucion': 14.2},
                    'venus': {'posicion': 'Sagitario', 'contribucion': 16.8},
                    'earth': {'posicion': 'Libra', 'contribucion': 9.5},
                    'mars': {'posicion': 'Cáncer', 'contribucion': 4.3},
                    'jupiter': {'posicion': 'Géminis', 'contribucion': 25.6},
                    'saturn': {'posicion': 'Piscis', 'contribucion': 12.7},
                    'uranus': {'posicion': 'Tauro', 'contribucion': 11.4},
                    'neptune': {'posicion': 'Aries', 'contribucion': 5.5}
                },
                'energias': {
                    'revelacion': 85,
                    'transformacion': 82,
                    'caos_creativo': 88,
                    'despertar': 90
                }
            },
            '2035_gran_alineacion': {
                'fecha': '2035-03-15',
                'ftrt': 5.161,
                'planetas': {
                    'mercury': {'posicion': 'Piscis', 'contribucion': 11.8},
                    'venus': {'posicion': 'Aries', 'contribucion': 14.5},
                    'earth': {'posicion': 'Acuario', 'contribucion': 8.9},
                    'mars': {'posicion': 'Capricornio', 'contribucion': 5.2},
                    'jupiter': {'posicion': 'Aries', 'contribucion': 32.7},
                    'saturn': {'posicion': 'Aries', 'contribucion': 18.3},
                    'uranus': {'posicion': 'Géminis', 'contribucion': 6.1},
                    'neptune': {'posicion': 'Aries', 'contribucion': 2.5}
                },
                'energias': {
                    'revolucion': 95,
                    'iniciacion': 92,
                    'ruptura_total': 96,
                    'renacimiento': 94
                }
            }
        }
    
    def calcular_comparativa_ftrt(self):
        """Calcula comparativa FTRT entre configuraciones clave"""
        print("📊 COMPARATIVA FTRT - CONFIGURACIONES HISTÓRICAS Y FUTURAS")
        print("=" * 70)
        
        datos = []
        for nombre, config in self.configuraciones_clave.items():
            datos.append({
                'Configuración': nombre.replace('_', ' ').title(),
                'Fecha': config['fecha'],
                'FTRT': config['ftrt'],
                'Energía Total': sum(config['energias'].values()) / 4
            })
        
        df = pd.DataFrame(datos)
        print(df.to_string(index=False))
        
        # Análisis comparativo
        print(f"\n🔍 ANÁLISIS COMPARATIVO:")
        print(f"   • 2003 vs 2024: FTRT {self.configuraciones_clave['2003_halloween']['ftrt']/self.configuraciones_clave['2024_mayo']['ftrt']:.1f}x mayor")
        print(f"   • 2035 proyectado: FTRT más alta registrada ({self.configuraciones_clave['2035_gran_alineacion']['ftrt']})")
        print(f"   • Q4 2025: 'Tormenta de Revelación' con FTRT {self.configuraciones_clave['2025_q4']['ftrt']}")
        
        return df
    
    def visualizar_ftrt_comparativa(self):
        """Crea visualización comparativa de FTRT"""
        nombres = []
        valores_ftrt = []
        colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
        
        for nombre, config in self.configuraciones_clave.items():
            nombres.append(nombre.replace('_', '\n').title())
            valores_ftrt.append(config['ftrt'])
        
        plt.figure(figsize=(12, 8))
        
        # Gráfico principal
        plt.subplot(2, 2, 1)
        bars = plt.bar(nombres, valores_ftrt, color=colores, alpha=0.8)
        plt.title('COMPARATIVA FTRT - CONFIGURACIONES CLAVE', fontsize=14, fontweight='bold')
        plt.ylabel('Fuerza de Marea Relativa Total (FTRT)')
        plt.xticks(rotation=45)
        
        # Añadir valores en las barras
        for bar, valor in zip(bars, valores_ftrt):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                    f'{valor:.3f}', ha='center', va='bottom', fontweight='bold')
        
        # Radar de energías
        plt.subplot(2, 2, 2)
        categorias = list(self.configuraciones_clave['2003_halloween']['energias'].keys())
        
        for i, (nombre, config) in enumerate(self.configuraciones_clave.items()):
            valores = list(config['energias'].values())
            # Cerrar el radar
            valores.append(valores[0])
            angulos = np.linspace(0, 2*np.pi, len(categorias), endpoint=False).tolist()
            angulos.append(angulos[0])
            
            plt.polar(angulos, valores, 'o-', linewidth=2, 
                     label=nombre.replace('_', ' ').title(), color=colores[i])
        
        plt.xticks(angulos[:-1], categorias)
        plt.title('RADAR DE ENERGÍAS PLANETARIAS', fontsize=12, fontweight='bold')
        plt.legend(bbox_to_anchor=(1.1, 1.05))
        
        # Contribución planetaria 2003
        plt.subplot(2, 2, 3)
        planetas = list(self.configuraciones_clave['2003_halloween']['planetas'].keys())
        contribuciones = [config['contribucion'] for config in self.configuraciones_clave['2003_halloween']['planetas'].values()]
        
        plt.pie(contribuciones, labels=planetas, autopct='%1.1f%%', startangle=90)
        plt.title('CONTRIBUCIÓN PLANETARIA - HALLOWEEN 2003', fontsize=12)
        
        # Contribución planetaria 2035
        plt.subplot(2, 2, 4)
        contribuciones_2035 = [config['contribucion'] for config in self.configuraciones_clave['2035_gran_alineacion']['planetas'].values()]
        
        plt.pie(contribuciones_2035, labels=planetas, autopct='%1.1f%%', startangle=90)
        plt.title('CONTRIBUCIÓN PLANETARIA - GRAN ALINEACIÓN 2035', fontsize=12)
        
        plt.tight_layout()
        plt.show()
    
    def analizar_configuracion_detallada(self, config_name):
        """Análisis detallado de una configuración específica"""
        config = self.configuraciones_clave[config_name]
        
        print(f"\n🔍 ANÁLISIS DETALLADO: {config_name.replace('_', ' ').title()}")
        print("=" * 60)
        print(f"Fecha: {config['fecha']}")
        print(f"FTRT: {config['ftrt']}")
        print(f"Nivel de alerta: {self._clasificar_alerta(config['ftrt'])}")
        
        print("\n🪐 CONFIGURACIÓN PLANETARIA:")
        for planeta, datos in config['planetas'].items():
            print(f"  {planeta.title():8} | {datos['posicion']:12} | {datos['contribucion']:5.1f}%")
        
        print(f"\n⚡ ENERGÍAS DOMINANTES:")
        for energia, valor in config['energias'].items():
            intensidad = "🟢" if valor < 70 else "🟡" if valor < 85 else "🟠" if valor < 95 else "🔴"
            print(f"  {energia.title():15} | {valor:3}% {intensidad}")
        
        # Interpretación astrológica
        self._interpretacion_astrologica(config_name, config)
    
    def _clasificar_alerta(self, ftrt):
        """Clasifica el nivel de alerta basado en FTRT"""
        if ftrt < 1.2:
            return "NORMAL 🟢"
        elif ftrt < 1.8:
            return "MODERADO 🟡"
        elif ftrt < 2.5:
            return "ELEVADO 🟠"
        elif ftrt < 4.0:
            return "CRÍTICO 🔴"
        else:
            return "EXTREMO 💜"
    
    def _interpretacion_astrologica(self, config_name, config):
        """Interpretación astrológica de la configuración"""
        print(f"\n🎭 INTERPRETACIÓN ASTROLÓGICA:")
        
        interpretaciones = {
            '2003_halloween': {
                'tema_principal': "MUERTE Y RENACIMIENTO - Transformación radical",
                'influencia_solar': "Tormentas extremas, eyecciones masivas de plasma",
                'impacto_psicologico': "Intensidad emocional, revelaciones profundas",
                'recomendacion': "Soltar estructuras caducas, abrazar el cambio"
            },
            '2024_mayo': {
                'tema_principal': "EXPANSIÓN Y ESTABILIDAD - Crecimiento con bases sólidas", 
                'influencia_solar': "Actividad moderada-alta, eyecciones dirigidas",
                'impacto_psicologico': "Confianza, expansión de conciencia",
                'recomendacion': "Construir sobre bases sólidas, expandir horizontes"
            },
            '2025_q4': {
                'tema_principal': "REVELACIÓN Y CAOS CREATIVO - Deconstrucción de paradigmas",
                'influencia_solar': "Tormentas geomagnéticas intensas, disruptivas",
                'impacto_psicologico': "Despertar espiritual, cuestionamiento de realidades",
                'recomendacion': "Flexibilidad mental, preparación para revelaciones"
            },
            '2035_gran_alineacion': {
                'tema_principal': "RENACIMIENTO GLOBAL - Nuevos paradigmas civilizatorios",
                'influencia_solar': "Evento Carrington-level, transformación total",
                'impacto_psicologico': "Conciencia colectiva expandida, unidad planetaria", 
                'recomendacion': "Preparación sistémica, visión de nuevo mundo"
            }
        }
        
        interpre = interpretaciones[config_name]
        for clave, valor in interpre.items():
            print(f"  • {clave.replace('_', ' ').title()}: {valor}")
    
    def generar_reporte_completo(self):
        """Genera reporte completo interactivo"""
        print("🌌 SISTEMA INTERACTIVO FTRT + ASTROLOGÍA INTEGRADA")
        print("=" * 70)
        
        # Comparativa FTRT
        self.calcular_comparativa_ftrt()
        
        # Análisis detallado de cada configuración
        for config_name in self.configuraciones_clave.keys():
            self.analizar_configuracion_detallada(config_name)
            print("\n" + "-" * 70)
        
        # Visualización
        print("\n📈 GENERANDO VISUALIZACIONES...")
        self.visualizar_ftrt_comparativa()
        
        # Conclusiones finales
        self._mostrar_conclusiones()

    def _mostrar_conclusiones(self):
        """Muestra conclusiones finales del análisis"""
        print("\n🌟 CONCLUSIONES CIENTÍFICO-ASTROLÓGICAS:")
        print("=" * 70)
        
        conclusiones = [
            "🔬 **Halloween 2003**: FTRT 4.878 - La combinación Júpiter en Leo + " +
            "configuración en Escorpio generó tormentas históricas",
            
            "🌍 **Mayo 2024**: FTRT 2.943 - Energía más estabilizadora pero con " +
            "potente componente de revelación en Tauro",
            
            "⚡ **Q4 2025**: FTRT 3.215 - 'Tormenta de Revelación' con baricentro " +
            "disperso y tríada Saturno-Neptuno-Urano",
            
            "🔥 **2035 Gran Alineación**: FTRT 5.161 - La más alta proyectada, " +
            "con conjunción Júpiter-Saturno en Aries iniciando nueva era"
        ]
        
        for conclusion in conclusiones:
            print(f"  {conclusion}")
        
        print(f"\n🎯 RECOMENDACIÓN GLOBAL:")
        print("  Implementar sistemas FTRT-aware en infraestructura crítica")
        print("  Desarrollar protocolos de resiliencia para eventos extremos")
        print("  Integrar conciencia helio-astrológica en planificación estratégica")

# Función principal interactiva
def ejecutar_analisis_interactivo():
    """Ejecuta el análisis interactivo completo"""
    analyzer = InteractiveFTRTAnalyzer()
    
    print("🌠 BIENVENIDO AL SISTEMA INTERACTIVO FTRT")
    print("==========================================")
    
    while True:
        print("\n¿Qué análisis deseas ejecutar?")
        print("1. 📊 Reporte completo (FTRT + Astrología)")
        print("2. 🔍 Análisis específico por configuración") 
        print("3. 📈 Visualización comparativa")
        print("4. 🎯 Solo conclusiones")
        print("5. 🚪 Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ").strip()
        
        if opcion == '1':
            analyzer.generar_reporte_completo()
        elif opcion == '2':
            print("\nConfiguraciones disponibles:")
            configs = list(analyzer.configuraciones_clave.keys())
            for i, config in enumerate(configs, 1):
                print(f"  {i}. {config.replace('_', ' ').title()}")
            seleccion = input("Selecciona configuración (1-4): ").strip()
            try:
                idx = int(seleccion) - 1
                if 0 <= idx < len(configs):
                    analyzer.analizar_configuracion_detallada(configs[idx])
                else:
                    print("❌ Selección inválida")
            except ValueError:
                print("❌ Entrada inválida")
        elif opcion == '3':
            analyzer.visualizar_ftrt_comparativa()
        elif opcion == '4':
            analyzer._mostrar_conclusiones()
        elif opcion == '5':
            print("👋 ¡Hasta pronto! Sistema FTRT interactivo cerrado.")
            break
        else:
            print("❌ Opción no válida. Por favor selecciona 1-5.")

if __name__ == "__main__":
    ejecutar_analisis_interactivo()
