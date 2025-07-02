from flask import Blueprint, request, jsonify
from app.controllers.categorias_controller import CategoriaController

categorias_bp = Blueprint('categorias', __name__, url_prefix='/categorias')

@categorias_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(CategoriaController.get_all())

@categorias_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(CategoriaController.get_one(id))

@categorias_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    return jsonify(CategoriaController.create(data))

@categorias_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    data["id"] = id
    return jsonify(CategoriaController.update(data))

@categorias_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(CategoriaController.delete(id))