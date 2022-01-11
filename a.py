#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  e.py

class Almacen:
    def __init__(self, id, nombre, descripcion, precio, cantidad=0):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        return

    def info(self):
        print(self.id+" - "+self.nombre)


class App:
    def __init__(self):
        self.nombre = []
        self.notas = []

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1. Cargar alumno nuevo")
            print("2. Listar alumnos")
            print("3. Lista de alumnos con notas mayores o igual a 7")
            print("4. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.notas_pass()

    def cargar(self):
        for x in range(5):
            nom = input("Ingrese el nombre del alumno: ")
            self.nombre.append(nom)
            no = float(input("Ingrese una calificación: "))
            self.notas.append(no)

    def listar(self):
        print("lISTADO DE ALUMNOS")
        for x in range(5):
            print(self.nombre[x], "-", self.notas[x])
        print("___::   o    ::___")

    def notas_pass(self):
        print("lISTADO DE ALUMNOS (+7)")
        for x in range(5):
            if self.notas[x] >= 7:
                print(self.nombre[x], "-", self.notas[x])
        print("___::   o    ::___")


alumno = Alumnos()
alumno.menu()
