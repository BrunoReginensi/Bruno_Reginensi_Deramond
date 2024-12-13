
import json
import os

Libros_File = "libros.json"
Autores_File = "autores.json"

def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            return json.load(f)
    else:
        return []

def guardar_datos(archivo, datos):
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)

def agregar_libro():
    libros = cargar_datos(Libros_File)
    titulo = input("Ingresa el Título del Libro: ")
    genero = input("Ingresa el género del libro: ")
    año = input("Ingresa el año de publicación del libro: ")
    autor = input("Ingresa el autor del libro: ")

    nuevo_libro = {
        "titulo": titulo,
        "genero": genero,
        "año": año,
        "autor": autor
    }
    libros.append(nuevo_libro)
    guardar_datos(Libros_File, libros)
    print("El libro ha sido agregado con éxito.\n")

def agregar_autor():
    autores = cargar_datos(Autores_File)
    nombre = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad del autor: ")

    nuevo_autor = {
        "nombre": nombre,
        "nacionalidad": nacionalidad
    }
    autores.append(nuevo_autor)
    guardar_datos(Autores_File, autores)
    print("El autor ha sido agregado con éxito.\n")

def mostrar_información():
    libros = cargar_datos(Libros_File)
    autores = cargar_datos(Autores_File)

    print("\n--- Libros ---")
    if libros:
        for libro in libros:
            print(f"Título: {libro['titulo']}, Género: {libro['genero']}, Año: {libro['año']}, Autor: {libro['autor']}")
    else:
        print("No hay libros registrados.")

    print("\n--- Autores ---")
    if autores:
        for autor in autores:
            print(f"Nombre: {autor['nombre']}, Nacionalidad: {autor['nacionalidad']}")
    else:
        print("No hay autores registrados.")
    print()

def main():
    while True:
        print("--- Libreria Bruno ---")
        print("1. Agregar libro")
        print("2. Agregar autor")
        print("3. Verificar registros")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            agregar_autor()
        elif opcion == '3':
            mostrar_información()
        elif opcion == '4':
            print("Cerrando la librería...")
            break
        else:
            print("La opción es inválida.\n")

if __name__ == '__main__':
    main()