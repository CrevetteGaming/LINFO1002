# Programme écrit par  Nicolas Swinnen , étudiant de l'EPL, faculté de l'Université Catholique de Louvain.
# Lien • Github : https://github.com/CrevetteGaming/LINFO1002

import sqlite3
import os

# extraction des données de db pour les utiliser dans les graphs 


class info:

    def __init__(self,db):
        '''
        initialisation des attributs de l'objet
        '''
        self.data_name = db

    def connection(self):
        '''
        Connection à la base de donnée
        '''
        self.conn = sqlite3.connect(self.data_name)


    def deconnection(self):
        '''
        deconnection de la base de donnée
        '''
        self.conn.close()

    def familles(self):
        '''
        Création d'une liste comportant toutes les familles
        '''
        familles = []
        with self.conn as cursor:
            for row in cursor.execute('SELECT id, nom FROM familles'):
                #print(row)
                familles.append(row)
            return familles

    def date_naissance(self):
        '''
        Liste des dates des naissances
        '''
        date_naissances = []
        with self.conn as cursor:
            for row in cursor.execute("SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id ORDER BY date"):
                #print(row)
                date_naissances.append(row)
            return date_naissances

    def animal_races_pourcentage(self):
        '''
        Genere une liste avec le pourcentage d'une type de race
        '''
        with self.conn as cursor:
            return cursor.execute("SELECT type_id, pourcentage FROM animaux_types").fetchall()     


# ----- Races  ----- #

def recuperation_animaux(self):
    '''  
    Liste des ids d'animaux dans la base de données
    '''
    with self.conn as cursor:
        cursor.execute("SELECT id FROM animaux")
        recuperation_animaux = cursor.fetchall()
        #for all in recuperation_animaux:
            #print(all)
        return recuperation_animaux

def recuperation_races(conn,d):
    '''
    Liste avec les races des vaches et le pourcentage d'heritage de l'animal
    '''

    with conn as cursor:
        return cursor.execute("SELECT type_id, pourcentage FROM animaux_types WHERE animal_id = ?",(d,)).fetchall()


def recuperation_parents(conn,d):
    '''
    Liste avec la race des parents
    '''
    with conn as cursor:
        return cursor.execute("SELECT pere_id, mere_id FROM animaux, animaux_velages, velages WHERE animaux.id = ? AND animaux.id = animaux_velages.animal_id AND animaux_velages.animal_id = velages.id",(d,)).fetchall()


def races_calculs(races_parents):
    '''
    Calcul les races avec le pourcentage de chaque animal avec la race des parents
    '''
    dic_races = {}
    for race in races_parents:
        dic_races[race[0]] = dic_races.get(race[0], 0)+ race[1]

    #convertir dic_races, un dictionnaire en une liste tuples et divise le pourcentage par 2
    d = []
    for race in dic_races.items():
        d.append((race[0], race[1] / 2))
    return d            

def liaisons_races(conn, animal_id, race):
    '''
    liste des races et leur pourcentage ajouter à la base de données
    '''
    for r in race:
        with conn as cursor:
            cursor.execute("INSERT INTO animaux_types VALUES (?, ?, ?)", (animal_id, r[0], r[1]))
            print(f"ajouté : id:{animal_id},type: {r[0]}, pourcentage: {r}")

def set_races(conn, animal_id):
    '''
    Verifie si les parents de la vache n'ont pas déja été calculé
    '''
    if type(animal_id) == tuple:
        idc = animal_id[0]
    else:
        idc = animal_id
    
    parents = recuperation_parents(conn,idc)

    if len(parents) == 0 : 
        return recuperation_races(conn,idc)

    father = parents[0][0]
    mom = parents[0][1]

    races_father= recuperation_races(conn, int(father)) 
    races_mom = recuperation_races(conn, int(mom))

    if len(races_mom) == 0:
        races_mom = set_races(conn, mom)

    if len(races_father) == 0:
        races_father = set_races(conn, father)

    races = races_calculs(races_mom + races_father)
    liaisons_races(conn, idc, races)

    return races

def generate_race(conn):
    '''
    Generer la race pour les animaux de la base de données
    '''
    animal_id = []
    with conn as cursor:
        for row in cursor.execute("SELECT id FROM animaux"):
            animal_id.append(row)

    #Chercher et recuperer la race de chaque vache dans la base de données à l'aide de l'id
    for id in animal_id:
        races = []
        races.append(recuperation_races(conn,id[0]))

        if races[0] == []:
            set_races(conn,id)


        
