from ..db import get_connection  # Asegurate de tener esta función común

class ProveedorModel:
    def __init__(self, id=None, nombre=None, telefono=None, direccion=None, email=None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def get_one(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
            (self.nombre, self.telefono, self.direccion, self.email)
        )
        conn.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return True

    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE PROVEEDORES SET nombre=%s, telefono=%s, direccion=%s, email=%s WHERE id=%s",
            (self.nombre, self.telefono, self.direccion, self.email, self.id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            id=data.get("id"),
            nombre=data.get("nombre"),
            telefono=data.get("telefono"),
            direccion=data.get("direccion"),
            email=data.get("email")
        )