from ..models.categorias_model import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        return CategoriaModel.get_all()

    @staticmethod
    def get_one(id):
        data = CategoriaModel.get_one(id)
        return data or {"error": "Categoría no encontrada"}

    @staticmethod
    def create(data):
        try:
            nueva = CategoriaModel.deserializar(data)
            if nueva.create():
                return nueva.serializar()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(data):
        try:
            cat = CategoriaModel.deserializar(data)
            if cat.id is None:
                return {"error": "Falta ID de categoría"}
            if cat.update():
                return cat.serializar()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            if CategoriaModel.delete(id):
                return {"message": f"Categoría {id} eliminada correctamente"}
        except Exception as e:
            return {"error": str(e)}