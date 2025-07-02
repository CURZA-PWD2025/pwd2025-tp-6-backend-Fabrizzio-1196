from ..models.marca_model import MarcaModel

class MarcaController:

    @staticmethod
    def get_all():
        return MarcaModel.get_all()

    @staticmethod
    def get_one(id):
        data = MarcaModel.get_one(id)
        return data or {"error": "Marca no encontrada"}

    @staticmethod
    def create(data):
        try:
            nueva = MarcaModel.deserializar(data)
            if nueva.create():
                return nueva.serializar()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(data):
        try:
            marca = MarcaModel.deserializar(data)
            if marca.id is None:
                return {"error": "Falta ID de marca"}
            if marca.update():
                return marca.serializar()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            if MarcaModel.delete(id):
                return {"message": f"Marca {id} eliminada correctamente"}
        except Exception as e:
            return {"error": str(e)}