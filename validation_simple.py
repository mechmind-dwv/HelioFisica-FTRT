"""
Validación Simplificada FTRT - Sin dependencias problemáticas
"""
import numpy as np
from datetime import datetime

# Datos históricos de ejemplo
HISTORICAL_DATA = [
    {'fecha': '1859-09-01', 'evento': 'Carrington', 'ftrt': 3.21, 'magnitud': 10.0},
    {'fecha': '2003-10-29', 'evento': 'Halloween', 'ftrt': 4.87, 'magnitud': 9.5},
    {'fecha': '2024-05-10', 'evento': 'Mayo 2024', 'ftrt': 1.34, 'magnitud': 8.9}
]

def validar_correlaciones():
    """Valida correlaciones básicas"""
    ftrt_vals = [d['ftrt'] for d in HISTORICAL_DATA]
    magnitud_vals = [d['magnitud'] for d in HISTORICAL_DATA]
    
    correlacion = np.corrcoef(ftrt_vals, magnitud_vals)[0,1]
    
    print("=== VALIDACIÓN FTRT SIMPLIFICADA ===")
    print(f"Correlación FTRT vs Magnitud: {correlacion:.3f}")
    print(f"Eventos analizados: {len(HISTORICAL_DATA)}")
    
    # Umbrales de alerta
    print("\n=== UMBRALES FTRT ===")
    print("NORMAL    < 0.8  🟢")
    print("MODERADO  0.8-1.2 🟡") 
    print("ELEVADO   1.2-1.8 🟠")
    print("CRÍTICO   1.8-2.5 🔴")
    print("EXTREMO   > 2.5  💜")

if __name__ == "__main__":
    validar_correlaciones()
