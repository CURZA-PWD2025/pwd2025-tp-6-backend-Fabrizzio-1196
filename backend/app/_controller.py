from ._model import get_connection

# Obtener todos los artículos
def obtener_articulos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT A.id, A.descripcion, A.precio, A.stock,
               M.nombre AS marca,
               P.nombre AS proveedor
        FROM ARTICULOS A
        JOIN MARCAS M ON A.marca_id = M.id
        JOIN PROVEEDORES P ON A.proveedor_id = P.id
    """)
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

# Obtener un artículo por ID
def obtener_articulo_por_id(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT A.id, A.descripcion, A.precio, A.stock,
               M.nombre AS marca,
               P.nombre AS proveedor
        FROM ARTICULOS A
        JOIN MARCAS M ON A.marca_id = M.id
        JOIN PROVEEDORES P ON A.proveedor_id = P.id
        WHERE A.id = %s
    """, (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return resultado

# Crear un nuevo artículo
def agregar_articulo(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data['descripcion'],
        data['precio'],
        data['stock'],
        data['marca_id'],
        data['proveedor_id']
    ))
    conn.commit()
    nuevo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return nuevo_id

# Actualizar un artículo
def actualizar_articulo(id, data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ARTICULOS
        SET descripcion = %s, precio = %s, stock = %s, marca_id = %s, proveedor_id = %s
        WHERE id = %s
    """, (
        data['descripcion'],
        data['precio'],
        data['stock'],
        data['marca_id'],
        data['proveedor_id'],
        id
    ))
    conn.commit()
    actualizado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return actualizado

# Eliminar un artículo
def eliminar_articulo(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
    conn.commit()
    eliminado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return eliminado