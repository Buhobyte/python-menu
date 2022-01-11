import sqlite3
from sqlite3 import Error


class Connect:
    def __init__(self):
        self.sql_connection('Almacen.db')
        return

    def sql_connection(self, file_name):
        try:
            self.conne = sqlite3.connect(file_name)
            self.sql_table()
            return self.conne
        except Error:
            print(Error)

    def sql_table(self):
        cursorObj = self.conne.cursor()
        cursorObj.execute(
            "CREATE TABLE IF NOT EXISTS Producto (id integer PRIMARY KEY AUTOINCREMENT,nombre text NOT NULL,descripcion text,precio real,cantidad integer,peso integer)")
        cursorObj.execute(
            "CREATE TABLE IF NOT EXISTS Cliente (codigo integer PRIMARY KEY AUTOINCREMENT,	cedula text NOT NULL,	nombre text,	telefono text,	direccion text)")
        self.conne.commit()

    def sql_insert(self, query):
        cursorObj = self.conne.cursor()
        cursorObj.execute(query)
        self.conne.commit()
