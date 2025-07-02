from flask import Blueprint, request, jsonify
from app.controllers.articulos_controller import ArticuloController

articulos_bp = Blueprint('articulos', __name__, url_prefix='/articulos')

@articulos_bp.route('/', methods=['GET'])
def get_all_articulos():
    return jsonify(ArticuloController.get_all())

@articulos_bp.route('/<int:id>', methods=['GET'])
def get_articulo(id):
    return jsonify(ArticuloController.get_one(id))

@articulos_bp.route('/', methods=['POST'])
def create_articulo():
    data = request.get_json()
    return jsonify(ArticuloController.create(data))

@articulos_bp.route('/<int:id>', methods=['PUT'])
def update_articulo(id):
    data = request.get_json()
    data['id'] = id
    return jsonify(ArticuloController.update(data))

@articulos_bp.route('/<int:id>', methods=['DELETE'])
def delete_articulo(id):
    return jsonify(ArticuloController.delete(id))