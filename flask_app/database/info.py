# extraction des données de db pour les utiliser dans les graphs 
# info https://docs.python.org/3/library/sqlite3.html

import sqlite3
from sqlite3 import Error

class info:

    def __init__(self,db):
        self.data_name = db

    def connection(self):      #connection à la db
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db)
        except Error as e:
            print(e)
        return self.conn

    def deconnection(self):
        self.conn.close()

    def familles(self):
        familles == []
        with self.conn as cursor:
            for row in cursor.execute('SELECT id, nom FROM familles'):
                print(row)
                familles.append(row)
            return familles