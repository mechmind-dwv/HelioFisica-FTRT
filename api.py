"""
API REST del Sistema FTRT
Autores: Benjamin Cabeza Duran / DeepSeek
Fecha: Octubre 2025
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from datetime import datetime
import traceback

from ftrt_core import FTRTCalculator
from utils.logger import ftrt_logger

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas
api = Api(app)

# Crear instancia global del calculador
calculador = FTRTCalculator()

class HealthCheck(Resource):
    def get(self):
        """Endpoint de verificación de salud del servicio"""
        return {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'service': 'FTRT-API',
            'version': '1.0.0'
        }

class FTRTCalculator_API(Resource):
    def get(self):
        """
        Calcula FTRT para una fecha específica
        
        Parámetros Query:
        - fecha: Fecha en formato YYYY-MM-DD (opcional, default=hoy)
        
        Returns:
            JSON con resultado del cálculo FTRT
        """
        try:
            # Obtener fecha del query string o usar hoy
            fecha_str = request.args.get('fecha', None)
            if fecha_str:
                fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            else:
                fecha = datetime.now()
            
            ftrt_logger.info(f"📊 Solicitud de cálculo FTRT para {fecha.strftime('%Y-%m-%d')}")
            
            # Calcular FTRT
            resultado = calculador.calcular_ftrt_total(fecha)
            
            # Generar respuesta
            response = {
                'success': True,
                'data': {
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'ftrt_normalizada': round(resultado['ftrt_normalizada'], 3),
                    'ftrt_total': resultado['ftrt_total'],
                    'contribuciones': {
                        k: round(v, 2) for k, v in resultado['contribuciones'].items()
                    },
                    'metodo': resultado['metodo']
                },
                'timestamp': datetime.now().isoformat()
            }
            
            return jsonify(response)
            
        except Exception as e:
            ftrt_logger.error(f"❌ Error en cálculo FTRT: {str(e)}")
            return jsonify({
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc()
            }), 500

class FTRTAlert_API(Resource):
    def get(self):
        """
        Genera alerta FTRT para una fecha específica
        
        Parámetros Query:
        - fecha: Fecha en formato YYYY-MM-DD (opcional, default=hoy)
        
        Returns:
            JSON con información de alerta
        """
        try:
            # Obtener fecha
            fecha_str = request.args.get('fecha', None)
            if fecha_str:
                fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            else:
                fecha = datetime.now()
            
            ftrt_logger.info(f"⚠️ Solicitud de alerta para {fecha.strftime('%Y-%m-%d')}")
            
            # Generar alerta
            alerta = calculador.generar_alerta(fecha)
            
            # Generar respuesta
            response = {
                'success': True,
                'data': {
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'nivel_riesgo': alerta['nivel_riesgo'],
                    'color_alerta': alerta['color_alerta'],
                    'ftrt_normalizada': round(alerta['ftrt_normalizada'], 3),
                    'metodo_calculo': alerta['metodo_calculo']
                },
                'timestamp': datetime.now().isoformat()
            }
            
            # Añadir contribuciones si están disponibles
            if 'contribuciones_principales' in alerta:
                response['data']['contribuciones_principales'] = {
                    k: round(v, 2) for k, v in alerta['contribuciones_principales'].items()
                }
            
            return jsonify(response)
            
        except Exception as e:
            ftrt_logger.error(f"❌ Error generando alerta: {str(e)}")
            return jsonify({
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc()
            }), 500

class FTRTPrediction_API(Resource):
    def get(self):
        """
        Genera predicción FTRT para un rango de fechas
        
        Parámetros Query:
        - fecha_inicio: Fecha inicial YYYY-MM-DD
        - dias: Número de días a predecir (default=30)
        
        Returns:
            JSON con predicciones diarias
        """
        try:
            # Obtener parámetros
            fecha_str = request.args.get('fecha_inicio', None)
            if fecha_str:
                fecha_inicio = datetime.strptime(fecha_str, '%Y-%m-%d')
            else:
                fecha_inicio = datetime.now()
            
            dias = int(request.args.get('dias', 30))
            
            ftrt_logger.info(f"🔮 Solicitud de predicción: {dias} días desde {fecha_inicio.strftime('%Y-%m-%d')}")
            
            # Calcular predicciones
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
            
            return jsonify({
                'success': True,
                'data': predicciones,
                'metadata': {
                    'fecha_inicio': fecha_inicio.strftime('%Y-%m-%d'),
                    'dias': dias,
                    'timestamp': datetime.now().isoformat()
                }
            })
            
        except Exception as e:
            ftrt_logger.error(f"❌ Error generando predicción: {str(e)}")
            return jsonify({
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc()
            }), 500

# Registrar rutas
api.add_resource(HealthCheck, '/health')
api.add_resource(FTRTCalculator_API, '/api/v1/ftrt/calcular')
api.add_resource(FTRTAlert_API, '/api/v1/ftrt/alerta')
api.add_resource(FTRTPrediction_API, '/api/v1/ftrt/prediccion')

if __name__ == '__main__':
    ftrt_logger.info("🚀 Iniciando API FTRT")
    app.run(host='0.0.0.0', port=5000, debug=True)