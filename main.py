# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import os
import sqlite3
from sqlite3 import Error

os.system("cls")

# Conectar

conne = sqlite3.connect('Almacen.db')
cursorObj = conne.cursor()
cursorObj.execute(
    "CREATE TABLE IF NOT EXISTS Producto (id integer PRIMARY KEY AUTOINCREMENT,nombre text NOT NULL,descripcion text,precio real,cantidad integer,peso integer)")
cursorObj.execute(
    "CREATE TABLE IF NOT EXISTS Cliente (codigo integer PRIMARY KEY AUTOINCREMENT,	cedula text NOT NULL,	nombre text,	telefono text,	direccion text)")
conne.commit()


def sql_insert(query):
    try:
        conne.execute(query)
        conne.commit()
    except:
        print(query)
        print(Error)


def sql_list(table):
    try:
        query = "select *from "+table
        return conne.execute(query)
    except:
        print(query)
        print(Error)


def sql_search(table, text):
    try:
        query = "select *from "+table+" where nombre like '%"+text+"%'"
        return conne.execute(query)
    except:
        print(query)
        print(Error)


def sql_update(query):
    try:
        conne.execute(query)
        conne.commit()
    except:
        print(query)
        print(Error)


def sql_delete(table, name_id, codigo):
    try:
        sql = "DELETE FROM "+table+" WHERE "+name_id+"=?"
        conne.execute(sql, (codigo,))
        conne.commit()
    except:
        print(sql)
        print(Error)

# == fin connect

# conexion = sqlite3.connect('Almacen.db')
# print('base de datos creada con exito ..')


# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE productos  (codigo VARCHAR(50), descripcion VARCHAR(50), precio INTIGER, cantidad INTIGER, color VARCHAR(50),tamaño VARCHAR( 50))')
# cursor.execute(
#     'CREATE TABLE clientes  (codigo VARCHAR(50), ci INTIGER, nombre VARCHAR(50),telefono VARCHAR(50),direccion VARCHAR( 50))')

class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad=0):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        return

    def info(self):
        print(self.id+" - "+self.nombre)


class Almacen:
    # atributos
    def __init__(self):
        self.producto = list()

    # metodos
    def menu(self):
        opcion = 0
        while opcion != 11:
            os.system("cls")
            print("1. Ingresar nuevo producto")
            print("2. Ingresar nuevo cliente")
            print("3. Listar productos")
            print('4.Listar clientes')
            print('5.Buscar productos')
            print('6.Buscar clientes')
            print('7.Modificar productos')
            print('8.Modificar clientes')
            print('9.Eliminar productos')
            print('10.Eliminar clientes')
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
        print(sql)
        sql_insert(sql)

        # con.sql_insert(con, sql)
        exit = input("creando ")

    def ingresar_cliente(self):
        cedula = input("Ingrese cedula del cliente: ")
        nombre = input("Ingrese nombre del cliente: ")
        telefono = input("Ingrese telefono del cliente: ")
        direccion = input("Ingrese direccion del cliente: ")

        sql = "INSERT INTO cliente (cedula,nombre,telefono,direccion) VALUES('" + \
            cedula+"','"+nombre+"','"+telefono+"','"+direccion+"')"
        print(sql)
        sql_insert(sql)

    def listar_producto(self):
        list_products = sql_list("Producto")
        for i in list_products:
            print(i)
        salida = input("continue ...")

    def listar_clientes(self):
        list_clients = sql_list("Cliente")
        for i in list_clients:
            print(i)
        salida = input("continue ...")

    def buscar_producto(self):
        text = input("Buscar : ")
        products = sql_search("Producto", text)

        for i in products:
            print(i)
        salida = input("continue ...")

    def buscar_clientes(self):
        text = input("Buscar : ")
        clients = sql_search("cliente", text)

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
        sql_update(sql)
        salida = input("Modificado ...")

    def modificar_cliente(self):
        self.listar_clientes()
        option = input("Ingrese id: ")

        name = input("Ingrese nombre del cliente: ")
        telefono = input("Ingrese telefono del cliente: ")

        sql = "UPDATE Cliente SET nombre = '"+name + \
            "', telefono = '"+telefono+"' WHERE codigo= '"+option+"'"
        sql_update(sql)
        salida = input("Modificado ...")

    def eliminar_producto(self):
        self.listar_producto()
        option = input("Ingrese codigo a eliminar: ")

        sql_delete("Producto", "id", option)
        salida = input("Eliminado ...")

    def eliminar_cliente(self):
        self.listar_clientes()
        option = input("Ingrese codigo a eliminar: ")

        sql_delete("Cliente", "codigo", option)
        salida = input("Eliminado ...")


almacen = Almacen()
almacen.menu()
conne.close()
