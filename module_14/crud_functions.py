# Для задачи "Продуктовая база".
import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')


def initiate_db():
    pass

def get_all_products():
    pass

connection.commit()
connection.close()
