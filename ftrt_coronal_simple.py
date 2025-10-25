#!/usr/bin/env python3
"""
FTRT + AGUJEROS CORONALES - PARA MI APRENDIZ ESPAÑOL 🌟
"""

import numpy as np
from datetime import datetime

# CLASE SIMPLE PARA AGUJEROS CORONALES
class AgujeroCoronalFacil:
    def __init__(self):
        self.planetas_coronales = {
            'JUPITER': 1.5,
            'SATURNO': 1.3, 
            'MARTE': 1.2,
            'VENUS': 1.1
        }
    
    def calcular_agujero(self, fecha, planeta="JUPITER"):
        """Cálculo fácil de agujeros coronales"""
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        
        # Día del año para variación
        dia_año = fecha.timetuple().tm_yday
        
        # Cálculo simple
        base = 0.3
        variacion = abs(np.sin(dia_año / 365 * 4 * np.pi)) * 0.4
        planeta_factor = self.planetas_coronales.get(planeta, 1.0)
        
        probabilidad = base + variacion * planeta_factor
        
        return {
            'fecha': fecha.strftime('%Y-%m-%d'),
            'planeta': planeta,
            'probabilidad_agujero': min(probabilidad, 0.95),
            'riesgo': self._clasificar_riesgo(probabilidad),
            'tipo': self._predecir_tipo(probabilidad)
        }
    
    def _clasificar_riesgo(self, prob):
        if prob < 0.4: return "BAJO 🟢"
        elif prob < 0.6: return "MEDIO 🟡" 
        elif prob < 0.8: return "ALTO 🟠"
        else: return "CRÍTICO 🔴"
    
    def _predecir_tipo(self, prob):
        if prob < 0.3: return "Pequeño transitorio"
        elif prob < 0.6: return "Agujero recurrente"
        else: return "Agujero grande + CME posible"

# USO SUPER FÁCIL
def main():
    print("🌌 FTRT + AGUJEROS CORONALES - FÁCIL")
    print("=" * 50)
    
    calculador = AgujeroCoronalFacil()
    
    # Fechas para probar
    fechas = ["2025-12-31", "2026-03-20", "2026-06-15"]
    
    for fecha in fechas:
        resultado = calculador.calcular_agujero(fecha, "JUPITER")
        print(f"\n📅 {resultado['fecha']}:")
        print(f"   Planeta: {resultado['planeta']}")
        print(f"   Probabilidad: {resultado['probabilidad_agujero']:.1%}")
        print(f"   Riesgo: {resultado['riesgo']}")
        print(f"   Tipo: {resultado['tipo']}")

if __name__ == "__main__":
    main()
