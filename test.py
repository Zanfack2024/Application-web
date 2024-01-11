import sqlite3
fichier="C:/Users/HP/Desktop/diane/test.sq3"
fichier="C:/Users/HP/Desktop/diane/test.db"
conn=sqlite3.connect(fichier)
cur =conn.cursor()
cur.execute("CREATE TABLE professeur (age INTEGER, nom TEXT, taille REAL)")