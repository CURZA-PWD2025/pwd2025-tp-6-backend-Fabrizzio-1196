from flask import Flask
from flask_cors import CORS

from .routes.categorias_routes import categorias_bp
from .routes.marca_routes import marcas_bp
from .routes.articulos_routes import articulos_bp
from .routes.proveedores_routes import proveedores_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  

    app.register_blueprint(categorias_bp)
    app.register_blueprint(marcas_bp)
    app.register_blueprint(articulos_bp)
    app.register_blueprint(proveedores_bp)

    return app

if __name__ == '_main_':
    app = create_app()
    app.run(debug=True)
