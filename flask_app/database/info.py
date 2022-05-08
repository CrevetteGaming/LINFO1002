# extraction des données de db pour les utiliser dans les graphs 
# info https://docs.python.org/3/library/sqlite3.html & https://flaskguide.readthedocs.io/en/latest/flask/flask2.html 
#      https://www.dbtales.com/convert-a-sql-query-result-to-a-list-in-python-mysql/ 

import sqlite3
import os
import pathlib
from flask import *

class info:

    def __init__(self,db):
        self.data_name = db
    def connection(self):      #connection à db
        self.conn = sqlite3.connect(self.data_name)

    def deconnection(self):    #deconnection db
        self.conn.close()

    def familles(self):
        '''
        Liste de toutes les familles
        '''
        familles = []
        with self.conn as cursor:
            for row in cursor.execute('SELECT id, nom FROM familles'):
                #print(row)
                familles.append(row)
            return familles

    def date_naissance(self):
        '''
        liste dates des naissances
        '''
        date_naissances = []
        with self.conn as cursor:
            for row in cursor.execute("SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id ORDER BY date"):
                #print(row)
                date_naissances.append(row)
            return date_naissances
