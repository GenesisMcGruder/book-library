import sqlite3
 
CONN = sqlite3.connect('scripture-hub-database.db')
CURSOR = CONN.cursor()