# integracion_ftrt_artefacto.py
import json
from datetime import datetime, timedelta

class IntegradorCosmico:
    def __init__(self):
        self.escala_armonica = {
            'SOL': 432.0,
            'MERCURIO': 144.0,    # 432 * 1/3
            'VENUS': 162.0,       # 432 * 3/8  
            'TIERRA': 172.8,      # 432 * 2/5
            'MARTE': 192.0,       # 432 * 4/9
            'JÚPITER': 54.0,      # 432 * 1/8
            'SATURNO': 86.4,      # 432 * 1/5
            'URANO': 61.7,        # 432 * ~1/7
            'NEPTUNO': 66.5       # 432 * ~2/13
        }
    
    def calcular_resonancia_ftrt(self, valor_ftrt):
        """Convierte FTRT a frecuencia resonante"""
        # Fórmula: f_resonante = f_base * (1 + log10(ftrt))
        import math
        if valor_ftrt <= 0:
            return self.escala_armonica['SOL']
        
        factor_resonancia = 1 + (math.log10(valor_ftrt) * 0.3)
        return self.escala_armonica['SOL'] * factor_resonancia
    
    def generar_datos_artefacto(self, predicciones_ftrt):
        """Convierte predicciones FTRT a datos para el Artefacto"""
        datos_artefacto = {
            'predicciones': [],
            'alertas_sonoras': [],
            'resonancias_planetarias': []
        }
        
        for pred in predicciones_ftrt:
            frecuencia = self.calcular_resonancia_ftrt(pred['ftrt'])
            
            # Determinar color basado en nivel de alerta
            if pred['ftrt'] > 2.0:
                color = '#FF0000'  # Rojo - EXTREMO
                sonido = 'alerta_extrema'
            elif pred['ftrt'] > 1.5:
                color = '#FFA500'  # Naranja - CRÍTICO
                sonido = 'alerta_critica'
            else:
                color = '#FFFF00'  # Amarillo - ELEVADO
                sonido = 'alerta_elevada'
            
            datos_artefacto['predicciones'].append({
                'fecha': pred['fecha'],
                'ftrt': pred['ftrt'],
                'frecuencia_resonante': frecuencia,
                'color_alerta': color,
                'planetas_criticos': pred.get('planetas', [])
            })
            
            datos_artefacto['alertas_sonoras'].append({
                'fecha': pred['fecha'],
                'frecuencia': frecuencia,
                'intensidad': min(pred['ftrt'] * 0.2, 1.0),
                'tipo_sonido': sonido
            })
        
        return datos_artefacto
    
    def exportar_para_artefacto(self, datos, archivo_salida='datos_ftrt_artefacto.json'):
        """Exporta datos en formato para el Artefacto Cósmico"""
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Datos exportados a: {archivo_salida}")
        return archivo_salida

# Ejemplo de uso
if __name__ == "__main__":
    integrador = IntegradorCosmico()
    
    # Datos de ejemplo basados en tu ejecución de FTRT
    predicciones_ejemplo = [
        {'fecha': '2025-03-20', 'ftrt': 18.555, 'planetas': ['JÚPITER', 'SATURNO']},
        {'fecha': '2025-06-25', 'ftrt': 2.688, 'planetas': ['VENUS', 'MARTE']},
        {'fecha': '2025-10-27', 'ftrt': 1.536, 'planetas': ['MERCURIO']},
        {'fecha': '2025-12-25', 'ftrt': 1.332, 'planetas': ['VENUS', 'JÚPITER']}
    ]
    
    datos_artefacto = integrador.generar_datos_artefacto(predicciones_ejemplo)
    archivo = integrador.exportar_para_artefacto(datos_artefacto)
    
    print("\n🎵 RESONANCIAS CALCULADAS:")
    for pred in datos_artefacto['predicciones']:
        print(f"📅 {pred['fecha']}: FTRT {pred['ftrt']:.3f} → {pred['frecuencia_resonante']:.1f} Hz")
