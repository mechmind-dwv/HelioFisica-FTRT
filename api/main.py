from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ftrt_core import FTRTCalculator
from config.global_variables import UMBRALES

app = FastAPI(
    title="FTRT API",
    description="API para predicción de actividad solar basada en configuraciones planetarias",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de datos
class FTRTResponse(BaseModel):
    fecha: datetime
    ftrt_valor: float
    nivel_riesgo: str
    contribuciones_planetarias: dict
    alerta: bool
    mensaje: str

class PrediccionPeriodo(BaseModel):
    fecha_inicio: datetime
    fecha_fin: datetime
    ftrt_max: float
    fecha_max: datetime
    alertas: list
    valores_diarios: list

# Inicializar calculador FTRT
calculator = FTRTCalculator()

@app.get("/")
async def root():
    return {
        "mensaje": "API FTRT - Sistema de Alerta Temprana Solar",
        "version": "1.0.0",
        "estado": "activo"
    }

@app.get("/ftrt/actual", response_model=FTRTResponse)
async def obtener_ftrt_actual():
    fecha_actual = datetime.now()
    try:
        resultado = calculator.calcular_ftrt_total(fecha_actual)
        ftrt = resultado['ftrt_normalizada']
        
        # Determinar nivel de riesgo
        nivel = "NORMAL"
        alerta = False
        for umbral, valor in UMBRALES.items():
            if ftrt >= valor:
                nivel = umbral.upper()
                if umbral in ['alto', 'extremo']:
                    alerta = True

        return FTRTResponse(
            fecha=fecha_actual,
            ftrt_valor=ftrt,
            nivel_riesgo=nivel,
            contribuciones_planetarias=resultado['contribuciones'],
            alerta=alerta,
            mensaje=f"FTRT Actual: {ftrt:.3f} - Nivel: {nivel}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ftrt/prediccion/{dias}", response_model=PrediccionPeriodo)
async def obtener_prediccion(dias: int):
    if dias < 1 or dias > 90:
        raise HTTPException(
            status_code=400, 
            detail="El período de predicción debe estar entre 1 y 90 días"
        )
    
    fecha_inicio = datetime.now()
    fecha_fin = fecha_inicio + timedelta(days=dias)
    valores_diarios = []
    alertas = []
    ftrt_max = 0
    fecha_max = fecha_inicio

    try:
        for i in range(dias):
            fecha = fecha_inicio + timedelta(days=i)
            resultado = calculator.calcular_ftrt_total(fecha)
            ftrt = resultado['ftrt_normalizada']
            
            valores_diarios.append({
                "fecha": fecha,
                "ftrt": ftrt
            })

            if ftrt > ftrt_max:
                ftrt_max = ftrt
                fecha_max = fecha

            # Verificar alertas
            if ftrt >= UMBRALES['alto']:
                alertas.append({
                    "fecha": fecha,
                    "ftrt": ftrt,
                    "nivel": "ALTO" if ftrt < UMBRALES['extremo'] else "EXTREMO"
                })

        return PrediccionPeriodo(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            ftrt_max=ftrt_max,
            fecha_max=fecha_max,
            alertas=alertas,
            valores_diarios=valores_diarios
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ftrt/historico/{fecha}")
async def obtener_historico(fecha: str):
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
        resultado = calculator.calcular_ftrt_total(fecha_dt)
        return resultado
    except ValueError:
        raise HTTPException(
            status_code=400, 
            detail="Formato de fecha inválido. Use YYYY-MM-DD"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))