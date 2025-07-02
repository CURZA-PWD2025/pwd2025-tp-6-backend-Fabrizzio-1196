from flask import Blueprint, request, jsonify
from .controllers.articulos_controller import ArticuloController
from flask import Blueprint
from .routes.articulos_routes import articulos_bp
from .routes.categorias_routes import categorias_bp
from .routes.marca_routes import marcas_bp
from .routes.proveedores_routes import proveedores_bp

# Creamos un blueprint principal que agrupa todos
routes = Blueprint('routes', __name__)
routes.register_blueprint(articulos_bp)
routes.register_blueprint(categorias_bp)
routes.register_blueprint(marcas_bp)
routes.register_blueprint(proveedores_bp)

articulos_bp = Blueprint("articulos", __name__, url_prefix="/articulos")

# GET 
@articulos_bp.route("/", methods=["GET"])
def get_all_articulos():
    return jsonify(ArticuloController.get_all())


@articulos_bp.route("/<int:id>", methods=["GET"])
def get_articulo(id):
    return jsonify(ArticuloController.get_one(id))

# POST 
@articulos_bp.route("/", methods=["POST"])
def create_articulo():
    data = request.get_json()
    return jsonify(ArticuloController.create(data)), 201

# PUT 
@articulos_bp.route("/<int:id>", methods=["PUT"])
def update_articulo(id):
    data = request.get_json()
    data["id"] = id 
    return jsonify(ArticuloController.update(data))

# DELETE 
@articulos_bp.route("/<int:id>", methods=["DELETE"])
def delete_articulo(id):
    return jsonify(ArticuloController.delete(id))

routes = articulos_bp  