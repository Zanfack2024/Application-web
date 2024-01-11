import sqlite3
fichier="C:/Users/HP/Desktop/rosy/SIGMA.sq3"
fichier="C:/Users/HP/Desktop/rosy/SIGMA.db"
conn=sqlite3.connect(fichier)
cur =conn.cursor()
cur.execute("CREATE TABLE professeur (age INTEGER, nom TEXT, taille REAL)")

