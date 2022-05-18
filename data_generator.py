import sqlite3
import random
import datetime
import time

con = sqlite3.connect("data.db")

cursor = con.cursor()

temperature = float(f"{random.randint(10, 30)}.{random.randint(0, 99)}")
ph = float(f"{random.randint(1, 14)}.{random.randint(0, 99)}")


def create_tables():
    # Temperature
    cursor.execute(
        """CREATE TABLE Temperature(
            id INT PRIMARY KEY,
            value FLOAT,
            date_time VARCHAR
        );"""
    )

    # Ph
    cursor.execute(
        """CREATE TABLE Ph(
            id INT PRIMARY KEY,
            value FLOAT
            date DATETIME
        );"""
    )

    # Water level
    cursor.execute(
        """CREATE TABLE Water(
            id INT PRIMARY KEY,
            value FLOAT
            date DATETIME
        );"""
    )

    # Lux
    cursor.execute(
        """CREATE TABLE Lux(
            id INT PRIMARY KEY,
            value INT
            date DATETIME
        );"""
    )


def delete_tables():
    cursor.execute(
        """DROP TABLE Lux ;"""
    )

    cursor.execute(
        """DROP TABLE Water ;"""
    )

    cursor.execute(
        """DROP TABLE Ph ;"""
    )

    cursor.execute(
        """DROP TABLE Temperature ;"""
    )



def update():
    now = str(time.strftime("%Y-%m-%d %H-%M-%S"))
    cursor.execute(
        """INSERT INTO Temperature(value, date_time)
        VALUES (18.4, "test");

        """
    )

def main():
    update()
    con.commit()
    


if __name__=="__main__":
    main()
