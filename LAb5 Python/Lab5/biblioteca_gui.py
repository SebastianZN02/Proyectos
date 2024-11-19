import tkinter as tk
from tkinter import messagebox
from biblioteca import insertar_prestamo, consultar_libros, actualizar_autor, borrar_estudiante

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Biblioteca")
root.geometry("600x400")

# Función para manejar el registro de préstamo
def registrar_prestamo():
    try:
        codigo_usuario = int(entry_codigo_usuario.get())
        codigo_ejemplar = int(entry_codigo_ejemplar.get())
        insertar_prestamo(codigo_usuario, codigo_ejemplar)
        messagebox.showinfo("Éxito", "Préstamo registrado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al registrar préstamo: {e}")

# Función para manejar la consulta de libros
def consultar_libros_gui():
    codigo_libro = entry_codigo_libro.get() or None
    titulo = entry_titulo.get() or None
    isbn = entry_isbn.get() or None
    paginas = entry_paginas.get() or None
    editorial = entry_editorial.get() or None

    try:
        # Mostrar resultados en una nueva ventana
        resultados = consultar_libros(codigo_libro, titulo, isbn, paginas, editorial)
        ventana_resultados = tk.Toplevel(root)
        ventana_resultados.title("Resultados de la consulta")
        for resultado in resultados:
            tk.Label(ventana_resultados, text=str(resultado)).pack()
    except Exception as e:
        messagebox.showerror("Error", f"Error al consultar libros: {e}")

# Función para manejar la actualización de autores
def actualizar_autor_gui():
    try:
        codigo_autor = int(entry_codigo_autor.get())
        nuevo_nombre = entry_nombre_autor.get()
        actualizar_autor(codigo_autor, nuevo_nombre)
        messagebox.showinfo("Éxito", f"Autor actualizado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar autor: {e}")

# Función para manejar la eliminación de estudiantes
def eliminar_estudiante_gui():
    try:
        codigo_usuario = int(entry_estudiante_codigo.get())
        borrar_estudiante(codigo_usuario)
        messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar estudiante: {e}")

# --- Crear widgets ---
# Registro de préstamo
frame_prestamo = tk.LabelFrame(root, text="Registrar Préstamo")
frame_prestamo.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(frame_prestamo, text="ID Usuario:").grid(row=0, column=0, padx=5, pady=5)
entry_codigo_usuario = tk.Entry(frame_prestamo)
entry_codigo_usuario.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_prestamo, text="ID Ejemplar:").grid(row=1, column=0, padx=5, pady=5)
entry_codigo_ejemplar = tk.Entry(frame_prestamo)
entry_codigo_ejemplar.grid(row=1, column=1, padx=5, pady=5)

btn_prestamo = tk.Button(frame_prestamo, text="Registrar Préstamo", command=registrar_prestamo)
btn_prestamo.grid(row=2, column=0, columnspan=2, pady=10)

# Consulta de libros
frame_consulta = tk.LabelFrame(root, text="Consultar Libros")
frame_consulta.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(frame_consulta, text="ID Libro:").grid(row=0, column=0, padx=5, pady=5)
entry_codigo_libro = tk.Entry(frame_consulta)
entry_codigo_libro.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_consulta, text="Título:").grid(row=1, column=0, padx=5, pady=5)
entry_titulo = tk.Entry(frame_consulta)
entry_titulo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_consulta, text="ISBN:").grid(row=2, column=0, padx=5, pady=5)
entry_isbn = tk.Entry(frame_consulta)
entry_isbn.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_consulta, text="Páginas:").grid(row=3, column=0, padx=5, pady=5)
entry_paginas = tk.Entry(frame_consulta)
entry_paginas.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_consulta, text="Editorial:").grid(row=4, column=0, padx=5, pady=5)
entry_editorial = tk.Entry(frame_consulta)
entry_editorial.grid(row=4, column=1, padx=5, pady=5)

btn_consulta = tk.Button(frame_consulta, text="Consultar Libros", command=consultar_libros_gui)
btn_consulta.grid(row=5, column=0, columnspan=2, pady=10)

# Actualización de autores
frame_autor = tk.LabelFrame(root, text="Actualizar Autor")
frame_autor.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(frame_autor, text="ID Autor:").grid(row=0, column=0, padx=5, pady=5)
entry_codigo_autor = tk.Entry(frame_autor)
entry_codigo_autor.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_autor, text="Nuevo Nombre:").grid(row=1, column=0, padx=5, pady=5)
entry_nombre_autor = tk.Entry(frame_autor)
entry_nombre_autor.grid(row=1, column=1, padx=5, pady=5)

btn_actualizar = tk.Button(frame_autor, text="Actualizar Autor", command=actualizar_autor_gui)
btn_actualizar.grid(row=2, column=0, columnspan=2, pady=10)

# Eliminación de estudiantes
frame_eliminar = tk.LabelFrame(root, text="Eliminar Estudiante")
frame_eliminar.pack(fill="both", expand="yes", padx=10, pady=5)

tk.Label(frame_eliminar, text="ID Estudiante:").grid(row=0, column=0, padx=5, pady=5)
entry_estudiante_codigo = tk.Entry(frame_eliminar)
entry_estudiante_codigo.grid(row=0, column=1, padx=5, pady=5)

btn_eliminar = tk.Button(frame_eliminar, text="Eliminar Estudiante", command=eliminar_estudiante_gui)
btn_eliminar.grid(row=1, column=0, columnspan=2, pady=10)

# Ejecutar el loop principal de Tkinter
root.mainloop()
