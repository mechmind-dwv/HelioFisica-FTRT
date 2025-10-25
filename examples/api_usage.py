"""
Ejemplo de uso de la API REST FTRT
"""

import requests
from datetime import datetime, timedelta
import json

def ejemplo_api():
    """Demostración de uso de la API FTRT"""
    BASE_URL = "http://localhost:5000"
    
    print("🌟 DEMOSTRACIÓN API FTRT")
    print("=" * 50)
    
    # 1. Verificar salud del servicio
    print("\n1. Health Check")
    response = requests.get(f"{BASE_URL}/health")
    print(json.dumps(response.json(), indent=2))
    
    # 2. Calcular FTRT para hoy
    print("\n2. Cálculo FTRT para hoy")
    response = requests.get(f"{BASE_URL}/api/v1/ftrt/calcular")
    result = response.json()
    print(json.dumps(result['data'], indent=2))
    
    # 3. Calcular FTRT para evento histórico
    print("\n3. Cálculo FTRT para Evento Carrington")
    response = requests.get(f"{BASE_URL}/api/v1/ftrt/calcular?fecha=1859-09-01")
    result = response.json()
    print(json.dumps(result['data'], indent=2))
    
    # 4. Obtener alerta actual
    print("\n4. Alerta actual")
    response = requests.get(f"{BASE_URL}/api/v1/ftrt/alerta")
    result = response.json()
    print(json.dumps(result['data'], indent=2))
    
    # 5. Obtener predicción para próximos días
    print("\n5. Predicción próximos 5 días")
    response = requests.get(f"{BASE_URL}/api/v1/ftrt/prediccion?dias=5")
    result = response.json()
    print(json.dumps(result['data'], indent=2))

if __name__ == "__main__":
    ejemplo_api()