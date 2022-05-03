import sqlite3

def main():

    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()

    with open("inginious.sql",'r') as file:
        content = file.read()
    cursor.executescript(content)
    conn.commit()
    
    files = ['insert_animaux_types.sql','insert_animaux_velages.sql', 'insert_animaux.sql', 'insert_complications.sql', 'insert_familles.sql', 'insert_types.sql', 'insert_velages_complications.sql', 'insert_velages.sql']

    for f in files:
        with open(f"1002-sql-data/{f}",'r') as file:
            insert_content = file.read()
            print(f"{f} : succes")
        cursor.executescript(insert_content)
        conn.commit()

    conn.close()

if __name__ == '__main__':
    main()