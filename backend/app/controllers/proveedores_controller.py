from ..models.proveedores_model import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        data = ProveedorModel.get_one(id)
        return data or {"error": "Proveedor no encontrado"}

    @staticmethod
    def create(data):
        try:
            nuevo = ProveedorModel.deserializar(data)
            if nuevo.create():
                return nuevo.serializar()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(data):
        try:
            prov = ProveedorModel.deserializar(data)
            if prov.id is None:
                return {"error": "Falta ID del proveedor"}
            if prov.update():
                return prov.serializar()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            if ProveedorModel.delete(id):
                return {"message": f"Proveedor {id} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        