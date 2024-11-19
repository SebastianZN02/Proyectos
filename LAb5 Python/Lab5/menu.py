from biblioteca import insertar_prestamo, consultar_libros, actualizar_autor, borrar_estudiante

def menu():
    while True:
        print("\n--- Menú de Gestión de Biblioteca ---")
        print("1. Insertar Préstamo de Libro")
        print("2. Consultar Libros")
        print("3. Actualizar Información de Autor")
        print("4. Eliminar Estudiante")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo_usuario = int(input("Ingrese el ID del usuario: "))
            codigo_ejemplar = int(input("Ingrese el ID del ejemplar: "))
            insertar_prestamo(codigo_usuario, codigo_ejemplar)
        elif opcion == "2":
            print("Deje en blanco los campos que no desea usar como filtro.")
            codigo_libro = input("Ingrese el ID del libro (opcional): ") or None
            titulo = input("Ingrese el título del libro (opcional): ") or None
            isbn = input("Ingrese el ISBN del libro (opcional): ") or None
            paginas = input("Ingrese la cantidad de páginas (opcional): ") or None
            editorial = input("Ingrese la editorial del libro (opcional): ") or None
            consultar_libros(codigo_libro, titulo, isbn, paginas, editorial)
        elif opcion == "3":
            codigo_autor = int(input("Ingrese el ID del autor: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del autor: ")
            actualizar_autor(codigo_autor, nuevo_nombre)
        elif opcion == "4":
            codigo_usuario = int(input("Ingrese el ID del estudiante: "))
            borrar_estudiante(codigo_usuario)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Inicia el menú
if __name__ == "__main__":
    menu()
