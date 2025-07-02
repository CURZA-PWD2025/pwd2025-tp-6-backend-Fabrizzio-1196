from app.models.articulos_model import ArticulosModel

class ArticuloController:

    @staticmethod
    def get_all():
        return ArticulosModel.get_all()

    @staticmethod
    def get_one(id):
        articulo = ArticulosModel.get_one(id)
        if articulo:
            return articulo
        else:
            return {"error": "Artículo no encontrado"}

    @staticmethod
    def create(data):
        try:
            nuevo = ArticulosModel.deserializar(data)
            resultado = nuevo.create()
            if resultado:
                return nuevo.serializar()
            else:
                return {"error": "No se pudo crear el artículo"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(data):
        try:
            articulo = ArticulosModel.deserializar(data)
            if articulo.id is None:
                return {"error": "Falta el ID del artículo"}
            resultado = articulo.update()
            if resultado:
                return articulo.serializar()
            else:
                return {"error": "No se pudo actualizar el artículo"}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            # Traemos el artículo primero
            data = ArticulosModel.get_one(id)
            if not data:
                return {"error": "Artículo no encontrado"}

            articulo = ArticulosModel.deserializar(data)
            resultado = articulo.delete()
            if resultado:
                return {"message": f"Artículo con ID {id} eliminado correctamente"}
            else:
                return {"error": "No se pudo eliminar el artículo"}
        except Exception as e:
            return {"error": str(e)}