import mysql.connector
from mysql.connector import Error

# Función para conectar a la base de datos
def conectar():
    """Establece la conexión a la base de datos."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='IF4100_TURRIALBA_B03103',
            user='root',  # Cambia si usas otro usuario
            password='sebas12345'  # Cambia por tu contraseña
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            db_info = connection.get_server_info()
            print(f"Versión del servidor MySQL: {db_info}")
            return connection
    except Error as e:
        print(f"Error al conectar: {e}")
        return None

# Función para insertar un préstamo
def insertar_prestamo(codigo_usuario, codigo_ejemplar):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "CALL InsertarPrestamo(%s, %s);"
            valores = (codigo_usuario, codigo_ejemplar)
            cursor.execute(query, valores)
            connection.commit()
            print("Préstamo registrado correctamente.")
        except Error as e:
            print(f"Error al registrar préstamo: {e}")
        finally:
            if connection.is_connected():
                connection.close()
                print("Conexión cerrada")


def consultar_libros(codigo_libro=None, titulo=None, isbn=None, paginas=None, editorial=None):
    """Consulta libros usando parámetros específicos."""
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()  # Usar el cursor normal
            query = "CALL ConsultarLibros(%s, %s, %s, %s, %s);"
            valores = (codigo_libro, titulo, isbn, paginas, editorial)

            # Mostrar la consulta generada
            consulta_ejecutada = query % tuple(
                repr(v) if v is not None else 'NULL' for v in valores
            )
            print("\nConsulta ejecutada:")
            print(consulta_ejecutada)

            # Ejecutar el procedimiento con multi=True
            cursor.execute(query, valores, multi=True)

            print("\nResultados de la consulta:")
            for result in cursor:
                if result.with_rows:  # Procesar solo los conjuntos de resultados con filas
                    filas = result.fetchall()
                    if filas:
                        for fila in filas:
                            print(fila)
                    else:
                        print("Sin filas en este conjunto de resultados.")
                else:
                    print("Este conjunto de resultados no contiene filas.")
        except Error as e:
            print(f"Error al consultar libros: {e}")
        finally:
            if connection.is_connected():
                connection.close()
                print("\nConexión cerrada")





# Función para actualizar información de autores
def actualizar_autor(codigo_autor, nuevo_nombre):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "CALL ActualizarAutor(%s, %s);"
            valores = (codigo_autor, nuevo_nombre)
            cursor.execute(query, valores)
            connection.commit()
            print(f"Autor con ID {codigo_autor} actualizado a '{nuevo_nombre}'.")
        except Error as e:
            print(f"Error al actualizar autor: {e}")
        finally:
            if connection.is_connected():
                connection.close()
                print("Conexión cerrada")

# Función para eliminar estudiantes
def borrar_estudiante(codigo_usuario):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "CALL BorrarEstudiante(%s);"
            valores = (codigo_usuario,)
            cursor.execute(query, valores)
            connection.commit()
            print(f"Estudiante con ID {codigo_usuario} eliminado.")
        except Error as e:
            print(f"Error al eliminar estudiante: {e}")
        finally:
            if connection.is_connected():
                connection.close()
                print("Conexión cerrada")
