from flask import Blueprint, request, jsonify
from ..controllers.marca_controller import MarcaController

marcas_bp = Blueprint('marcas', __name__, url_prefix='/marcas')

@marcas_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(MarcaController.get_all())

@marcas_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(MarcaController.get_one(id))

@marcas_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    return jsonify(MarcaController.create(data))

@marcas_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    data["id"] = id
    return jsonify(MarcaController.update(data))

@marcas_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(MarcaController.delete(id))