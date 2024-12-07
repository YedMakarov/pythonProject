# Для задачи "Продуктовая база".
import sqlite3


def initiate_db():
    connection = sqlite3.connect("products_14_5.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    # Создание таблицы Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT  NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER DEFAULT 1000
    );
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
    connection = sqlite3.connect("products_14_5.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    results = cursor.fetchall()
    connection.close()

    return results


# Новая функция
def add_user(username: str, email: str, age: int):
    connection = sqlite3.connect("products_14_5.db")
    cursor = connection.cursor()

    cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?,?,?)",
                   (username, email, age))

    connection.commit()
    connection.close()


# Новая функция
def is_included(username: str):
    connection = sqlite3.connect("products_14_5.db")
    cursor = connection.cursor()

    cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
    results = cursor.fetchall()
    connection.close()

    if not results:
        return False
    else:
        return True
