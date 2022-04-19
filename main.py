import sqlite3

con = sqlite3.connect("data.db")

cursor = con.cursor()

cursor.execute("""CREATE TABLE Temperature(
temperature float,
time_taken time
);""")
