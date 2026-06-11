"""
API REST del Sistema FTRT
Autores: Benjamin Cabeza Duran / DeepSeek
Fecha: Octubre 2025
"""

from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from datetime import datetime, timedelta
import traceback

from ftrt_core import FTRTCalculator
from utils.logger import ftrt_logger

app = Flask(__name__)
CORS(app)
api = Api(app)

calculador = FTRTCalculator()

class HealthCheck(Resource):
    def get(self):
        return {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'service': 'FTRT-API',
            'version': '1.0.0'
        }

class FTRTCalculator_API(Resource):
    def get(self):
        try:
            fecha_str = request.args.get('fecha', None)
            if fecha_str:
                fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            else:
                fecha = datetime.now()

            ftrt_logger.info(f"📊 Solicitud de cálculo FTRT para {fecha.strftime('%Y-%m-%d')}")
            resultado = calculador.calcular_ftrt_total(fecha)

            response = {
                'success': True,
                'data': {
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'ftrt_normalizada': round(resultado['ftrt_normalizada'], 3),
                    'ftrt_total': resultado['ftrt_total'],
                    'contribuciones': {k: round(v, 2) for k, v in resultado['contribuciones'].items()},
                    'metodo': 'FTRT Standard'
                },
                'timestamp': datetime.now().isoformat()
            }
            return response, 200

        except Exception as e:
            ftrt_logger.error(f"❌ Error en cálculo FTRT: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc()
            }, 500

class FTRTAlert_API(Resource):
    def get(self):
        try:
            fecha_str = request.args.get('fecha', None)
            if fecha_str:
                fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            else:
                fecha = datetime.now()

            ftrt_logger.info(f"⚠️ Solicitud de alerta para {fecha.strftime('%Y-%m-%d')}")
            alerta = calculador.generar_alerta(fecha)

            response = {
                'success': True,
                'data': {
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'nivel_riesgo': alerta['nivel_riesgo'],
                    'color_alerta': alerta['color_alerta'],
                    'ftrt_normalizada': round(alerta['ftrt_normalizada'], 3),
                    'metodo_calculo': 'FTRT Standard'
                },
                'timestamp': datetime.now().isoformat()
            }

            if 'contribuciones_principales' in alerta:
                response['data']['contribuciones_principales'] = {
                    k: round(v, 2) for k, v in alerta['contribuciones_principales'].items()
                }

            return response, 200

        except Exception as e:
            ftrt_logger.error(f"❌ Error generando alerta: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc()
            }, 500

class FTRTPrediction_API(Resource):
    def get(self):
        try:
            fecha_str = request.args.get('fecha_inicio', None)
            if fecha_str:
                fecha_inicio = datetime.strptime(fecha_str, '%Y-%m-%d')
            else:
                fecha_inicio = datetime.now()

            dias = int(request.args.get('dias', 30))

            ftrt_logger.info(f"🔮 Solicitud de predicción: {dias} días desde {fecha_inicio.strftime('%Y-%m-%d')}")

            predicciones = []
            for i in range(dias):
                fecha = fecha_inicio + timedelta(days=i)
                resultado = calculador.calcular_ftrt_total(fecha)
                alerta = calculador.generar_alerta(fecha)

                predicciones.append({
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'ftrt_normalizada': round(resultado['ftrt_normalizada'], 3),
                    'nivel_riesgo': alerta['nivel_riesgo'],
                    'color_alerta': alerta['color_alerta']
                })

            response = {
                'success': True,
                'data': predicciones,
                'metadata': {
                    'fecha_inicio': fecha_inicio.strftime('%Y-%m-%d'),
                    'dias': dias,
                    'timestamp': datetime.now().isoformat()
                }
            }
            return response, 200

        except Exception as e:
            ftrt_logger.error(f"❌ Error generando predicción: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc()
            }, 500

# Registrar rutas
api.add_resource(HealthCheck, '/health')
api.add_resource(FTRTCalculator_API, '/api/v1/ftrt/calcular')
api.add_resource(FTRTAlert_API, '/api/v1/ftrt/alerta')
api.add_resource(FTRTPrediction_API, '/api/v1/ftrt/prediccion')

if __name__ == '__main__':
    ftrt_logger.info("🚀 Iniciando API FTRT")
    app.run(host='0.0.0.0', port=5000, debug=True)
