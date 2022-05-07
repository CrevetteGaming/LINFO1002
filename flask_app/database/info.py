# extraction des données de db pour les utiliser dans les graphs 
# info https://docs.python.org/3/library/sqlite3.html

import sqlite3
import os
import pathlib

class info:

    def __init__(self,db):
        self.data_name = db

    def connection(self):      #connection à la db
        self.conn = sqlite3.connect(self.data_name)

    
    def deconnection(self):
        self.conn.close()

    def familles(self):
        familles = []
        with self.conn as cursor:
            for row in cursor.execute('SELECT id, nom FROM familles'):
                print(row)
                familles.append(row)
            return familles

