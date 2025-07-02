from app.db import get_connection

class ArticulosModel:
    def _init_(self, id, descripcion, precio, stock, marca_id, proveedor_id):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT 
                a.id, a.descripcion, a.precio, a.stock,
                m.nombre AS marca,
                p.nombre AS proveedor,
                c.nombre AS categoria
            FROM ARTICULOS a
            JOIN MARCAS m ON a.marca_id = m.id
            JOIN PROVEEDORES p ON a.proveedor_id = p.id
            LEFT JOIN ARTICULOS_CATEGORIAS ac ON a.id = ac.articulo_id
            LEFT JOIN CATEGORIAS c ON ac.categoria_id = c.id
            ORDER BY a.id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        articulos = {}
        for row in rows:
            articulo_id = row["id"]
            if articulo_id not in articulos:
                articulos[articulo_id] = {
                    "id": row["id"],
                    "descripcion": row["descripcion"],
                    "precio": row["precio"],
                    "stock": row["stock"],
                    "marca": row["marca"],
                    "proveedor": row["proveedor"],
                    "categorias": []
                }
            categoria = row["categoria"]
            if categoria and categoria not in articulos[articulo_id]["categorias"]:
                articulos[articulo_id]["categorias"].append(categoria)

        return list(articulos.values())

    @staticmethod
    def get_one(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT 
                a.id, a.descripcion, a.precio, a.stock,
                m.nombre AS marca,
                p.nombre AS proveedor,
                c.nombre AS categoria
            FROM ARTICULOS a
            JOIN MARCAS m ON a.marca_id = m.id
            JOIN PROVEEDORES p ON a.proveedor_id = p.id
            LEFT JOIN ARTICULOS_CATEGORIAS ac ON a.id = ac.articulo_id
            LEFT JOIN CATEGORIAS c ON ac.categoria_id = c.id
            WHERE a.id = %s;
        """
        cursor.execute(query, (id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        if not rows:
            return None

        result = {
            "id": rows[0]["id"],
            "descripcion": rows[0]["descripcion"],
            "precio": rows[0]["precio"],
            "stock": rows[0]["stock"],
            "marca": rows[0]["marca"],
            "proveedor": rows[0]["proveedor"],
            "categorias": []
        }

        for row in rows:
            categoria = row["categoria"]
            if categoria and categoria not in result["categorias"]:
                result["categorias"].append(categoria)

        return result