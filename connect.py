import sqlite3
from sqlite3 import Error


class Connect:
    def __init__(self, file_name):
        self.conne = sqlite3.connect(file_name)
        self.sql_create_table()

    def sql_create_table(self):
        try:
            cursorObj = self.conne.cursor()
            cursorObj.execute(
                "CREATE TABLE IF NOT EXISTS Producto (id integer PRIMARY KEY AUTOINCREMENT,nombre text NOT NULL,descripcion text,precio real,cantidad integer,peso integer)")
            cursorObj.execute(
                "CREATE TABLE IF NOT EXISTS Cliente (codigo integer PRIMARY KEY AUTOINCREMENT,	cedula text NOT NULL,	nombre text,	telefono text,	direccion text)")
            self.conne.commit()
        except:
            print(Error)

    def sql_insert(self, query):
        try:
            self.conne.execute(query)
            self.conne.commit()
        except:
            print(query)
            print(Error)

    def sql_insert(self, query):
        try:
            self.conne.execute(query)
            self.conne.commit()
        except:
            print(query)
            print(Error)

    def sql_list(self, table):
        try:
            query = "select *from "+table
            return self.conne.execute(query)
        except:
            print(query)
            print(Error)

    def sql_search(self, table, text):
        try:
            query = "select *from "+table+" where nombre like '%"+text+"%'"
            return self.conne.execute(query)
        except:
            print(query)
            print(Error)

    def sql_update(self, query):
        try:
            self.conne.execute(query)
            self.conne.commit()
        except:
            print(query)
            print(Error)

    def sql_delete(self, table, name_id, codigo):
        try:
            sql = "DELETE FROM "+table+" WHERE "+name_id+"=?"
            self.conne.execute(sql, (codigo,))
            self.conne.commit()
        except:
            print(sql)
            print(Error)
