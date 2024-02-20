import sqlite3

conn = sqlite3.connect('furnizori.db')

c = conn.cursor()

c.execute("""CREATE TABLE furnizori(
        id text PRIMARY KEY,
        nume text NOT NULL,
        numar_telefon text NOT NULL       
)""")

def search_database(d_search):
    c.execute(f"""SELECT * FROM furnizori WHERE nume = {d_search}""")

