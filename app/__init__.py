from flask import Flask

# Importar cada blueprint
from app.routes.articulos_routes import articulos_bp
from app.routes.categorias_routes import categorias_bp
from app.routes.proveedores_routes import proveedores_bp
from app.routes.marca_routes import marcas_bp

def create_app():
    app = Flask(__name__)

    # Registrar cada blueprint por separado
    app.register_blueprint(articulos_bp)
    app.register_blueprint(categorias_bp)
    app.register_blueprint(proveedores_bp)
    app.register_blueprint(marcas_bp)

    return app