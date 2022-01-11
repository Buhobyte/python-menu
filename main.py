# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import os
import sqlite3
from sqlite3 import Error
from connect import Connect
import pandas as pd
from tabulate import tabulate

os.system("cls")

# Conectar

class Almacen:
    # atributos
    def __init__(self, conne):
        self.conne = conne
        self.productos = list()

    # metodos
    def menu(self):
        opcion = 0
        while opcion != 11:
            os.system("cls")
            print("1. Ingresar nuevo producto")
            print("2. Ingresar nuevo cliente")
            print("3. Listar productos")
            print('4. Listar clientes')
            print('5. Buscar productos')
            print('6. Buscar clientes')
            print('7. Modificar productos')
            print('8. Modificar clientes')
            print('9. Eliminar productos')
            print('10. Eliminar clientes')
            print("11. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                self.ingresar_producto()

            elif opcion == 2:
                self.ingresar_cliente()

            elif opcion == 3:
                self.listar_producto()

            elif opcion == 4:
                self.listar_clientes()

            elif opcion == 5:
                self.buscar_producto()

            elif opcion == 6:
                self.buscar_clientes()

            elif opcion == 7:
                self.modificar_producto()

            elif opcion == 8:
                self.modificar_cliente()

            elif opcion == 9:
                self.eliminar_producto()

            elif opcion == 10:
                self.eliminar_cliente()

            elif opcion == 11:
                print('Saliendo ...')

    def ingresar_producto(self):
        name = input("Ingrese nombre del producto: ")
        descrip = input("Ingrese descripcion del producto: ")
        price = input("Ingrese precio del producto: ")
        count = input("Ingrese cantidad del producto: ")
        weigth = input("Ingrese peso del producto: ")

        sql = "INSERT INTO Producto (nombre,descripcion,precio,cantidad ,peso) VALUES('" + \
            name+"','"+descrip+"',"+price+","+count+","+weigth+")"
        self.conne.sql_insert(sql)

        # con.self.conne.sql_insert(con, sql)
        exit = input("creando ")

    def ingresar_cliente(self):
        cedula = input("Ingrese cedula del cliente: ")
        nombre = input("Ingrese nombre del cliente: ")
        telefono = input("Ingrese telefono del cliente: ")
        direccion = input("Ingrese direccion del cliente: ")

        sql = "INSERT INTO cliente (cedula,nombre,telefono,direccion) VALUES('" + \
            cedula+"','"+nombre+"','"+telefono+"','"+direccion+"')"
        self.conne.sql_insert(sql)
        salida = input("continue ...")

    def listar_producto(self):
        list_products = self.conne.sql_list("Producto")

        df = pd.DataFrame(list_products, columns=[
                          'ID', 'Name', 'Descrip', 'Precio', 'Cant', 'Peso'])
        print("=================== Productos ========================")
        print(df)
        print("======================================================")
        salida = input("continue ...")

    def listar_clientes(self):
        list_clients = self.conne.sql_list("Cliente")
        print("\n=================== Clientes =========================")
        print(tabulate(list_clients, headers=[
              'ID', 'Name', 'Descrip', 'Precio', 'Cant', 'Peso']))
        print("======================================================")
        salida = input("continue ...")

    def buscar_producto(self):
        text = input("Buscar : ")
        products = self.conne.sql_search("Producto", text)

        for i in products:
            print(i)
        salida = input("continue ...")

    def buscar_clientes(self):
        text = input("Buscar : ")
        clients = self.conne.sql_search("cliente", text)

        for i in clients:
            print(i)
        salida = input("continue ...")

    def modificar_producto(self):
        self.listar_producto()
        option = input("Ingrese id: ")

        name = input("Ingrese nombre del producto: ")
        descrip = input("Ingrese descripcion del producto: ")

        sql = "UPDATE Producto SET nombre = '"+name + \
            "', descripcion = '"+descrip+"' WHERE id= '"+option+"'"
        self.conne.sql_update(sql)
        salida = input("Modificado ...")

    def modificar_cliente(self):
        self.listar_clientes()
        option = input("Ingrese id: ")

        name = input("Ingrese nombre del cliente: ")
        telefono = input("Ingrese telefono del cliente: ")

        sql = "UPDATE Cliente SET nombre = '"+name + \
            "', telefono = '"+telefono+"' WHERE codigo= '"+option+"'"
        self.conne.sql_update(sql)
        salida = input("Modificado ...")

    def eliminar_producto(self):
        self.listar_producto()
        option = input("Ingrese codigo a eliminar: ")

        self.conne.sql_delete("Producto", "id", option)
        salida = input("Eliminado ...")

    def eliminar_cliente(self):
        self.listar_clientes()
        option = input("Ingrese codigo a eliminar: ")

        self.conne.sql_delete("Cliente", "codigo", option)
        salida = input("Eliminado ...")


connection = Connect('Almacen.db')
almacen = Almacen(connection)
almacen.menu()
connection.conne.close()
