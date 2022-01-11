import sqlite3

# conexion = sqlite3.connect('Almacen.db')
# print('base de datos creada con exito ..')


# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE productos  (codigo VARCHAR(50), descripcion VARCHAR(50), precio INTIGER, cantidad INTIGER, color VARCHAR(50),tamaño VARCHAR( 50))')
# cursor.execute(
#     'CREATE TABLE clientes  (codigo VARCHAR(50), ci INTIGER, nombre VARCHAR(50),telefono VARCHAR(50),direccion VARCHAR( 50))')


class Almacen:
    def __init__(self):
        self.codigo = []
        self.descripc


print("PROGRAMACION II")

print("Menu de Opciones")
print("1. Verifica si la cadena empieza por minuscula")
print("2. Confirma si el numero es perfecto")
print("3. lista con los números perfectos comprendidos entre 1 y n")
print("4. Salir")
print()

opc = int(input(("Elija su opcion: ")))
print()

while opc != 4:
    if opc == 1:
        print("INICIO DE FRASE CON MINUSCULA ?")
