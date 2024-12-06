# Для задачи "Продуктовая база".
import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)",
                   ("Продукт 1", "Описание 1", "100"))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)",
                   ("Продукт 2", "Описание 2", "200"))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)",
                   ("Продукт 3", "Описание 3", "300"))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)",
                   ("Продукт 4", "Описание 4", "400"))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    results = cursor.fetchall()

    return results

