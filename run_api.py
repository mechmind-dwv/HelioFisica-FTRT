"""
Script de inicio de API FTRT en producción
"""

import os
from gunicorn.app.base import BaseApplication
from api import app
from utils.logger import ftrt_logger

class FTRTApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    # Configuración de gunicorn
    options = {
        'bind': '0.0.0.0:5000',
        'workers': 4,
        'worker_class': 'gevent',
        'timeout': 120,
        'keepalive': 5,
        'errorlog': 'logs/gunicorn_error.log',
        'accesslog': 'logs/gunicorn_access.log',
        'loglevel': 'info',
    }

    ftrt_logger.info("🚀 Iniciando API FTRT en producción")
    FTRTApplication(app, options).run()