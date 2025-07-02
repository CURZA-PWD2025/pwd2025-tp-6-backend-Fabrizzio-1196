from flask import Blueprint, request, jsonify
from ..controllers.proveedores_controller import ProveedorController

proveedores_bp = Blueprint('proveedores', __name__, url_prefix='/proveedores')

@proveedores_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(ProveedorController.get_all())

@proveedores_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(ProveedorController.get_one(id))

@proveedores_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    return jsonify(ProveedorController.create(data))

@proveedores_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    data["id"] = id
    return jsonify(ProveedorController.update(data))

@proveedores_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(ProveedorController.delete(id))