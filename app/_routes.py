from flask import Blueprint, request, jsonify
from app.controllers.articulos_controller import ArticuloController

articulos_bp = Blueprint("articulos", __name__, url_prefix="/articulos")

# GET 
@articulos_bp.route("/", methods=["GET"])
def get_all_articulos():
    return jsonify(ArticuloController.get_all())

# GET 
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