import sqlite3
import sys


# Conexión a la base de datos SQLite
def connect():
    return sqlite3.connect('biblioteca.db')


# Creación de la tabla si no existe
def crear_tabla():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        anio INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()


# Agregar nuevo libro
def agregar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    anio = input("Año de publicación: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)", (titulo, autor, anio))
    conn.commit()
    conn.close()
    print(f"Libro '{titulo}' agregado exitosamente.")


# Actualizar libro existente
def actualizar_libro():
    id_libro = input("ID del libro a actualizar: ")
    titulo = input("Nuevo título del libro: ")
    autor = input("Nuevo autor del libro: ")
    anio = input("Nuevo año de publicación: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE libros SET titulo = ?, autor = ?, anio = ? WHERE id = ?", (titulo, autor, anio, id_libro))
    conn.commit()
    conn.close()
    print(f"Libro ID '{id_libro}' actualizado exitosamente.")


# Eliminar libro existente
def eliminar_libro():
    id_libro = input("ID del libro a eliminar: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conn.commit()
    conn.close()
    print(f"Libro ID '{id_libro}' eliminado exitosamente.")


# Ver listado de libros
def ver_libros():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, anio FROM libros")
    libros = cursor.fetchall()
    conn.close()

    if libros:
        print("Listado de libros:")
        for libro in libros:
            print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Año: {libro[3]}")
    else:
        print("No hay libros en la biblioteca.")


# Buscar libro por título
def buscar_libro():
    titulo = input("Título del libro a buscar: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, autor, anio FROM libros WHERE titulo LIKE ?", ('%' + titulo + '%',))
    libro = cursor.fetchall()
    conn.close()

    if libro:
        print("Libros encontrados:")
        for l in libro:
            print(f"ID: {l[0]}, Autor: {l[1]}, Año: {l[2]}")
    else:
        print("No se encontraron libros con ese título.")


# Función principal del menú
def menu():
    crear_tabla()  # Asegurar que la tabla de libros exista
    while True:
        print("\n--- Biblioteca de Libros ---")
        print("1. Agregar nuevo libro")
        print("2. Actualizar libro existente")
        print("3. Eliminar libro existente")
        print("4. Ver listado de libros")
        print("5. Buscar libro por título")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            actualizar_libro()
        elif opcion == '3':
            eliminar_libro()
        elif opcion == '4':
            ver_libros()
        elif opcion == '5':
            buscar_libro()
        elif opcion == '6':
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
