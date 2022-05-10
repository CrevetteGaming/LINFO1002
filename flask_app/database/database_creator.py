#création de la base de données             info: https://python.doctor/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite
import sqlite3
from info import generate_race
import os
import pathlib

def main():
    
    files = ['insert_animaux_types.sql','insert_animaux_velages.sql', 'insert_animaux.sql', 'insert_complications.sql', 'insert_familles.sql', 'insert_types.sql', 'insert_velages_complications.sql', 'insert_velages.sql']

    conn = sqlite3.connect(os.path.join(pathlib.Path(__file__).parent.absolute(), "database.sqlite"))      #accès à la base de données
    cursor = conn.cursor()                      #le curseur p

    
    with open("inginious.sql",'r') as file:     #creation de la db
        content = file.read()
    cursor.executescript(content)
    conn.commit()
    
    for f in files:
        with open(f"1002-sql-data/{f}",'r') as file:
            insert_content = file.read()
        cursor.executescript(insert_content)
        conn.commit()

    #rajouter l'héritage génétique 
    generate_race(conn)

    conn.close() #fermeture db 

                                             

if __name__ == '__main__':
    main()