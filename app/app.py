from flask import Flask
from app._routes import routes  # Importa desde app._routes si _routes.py está en app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app
