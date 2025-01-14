# Задача "Средний баланс пользователя".


import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
#                ("username", "example@gmail.com", "10", "1000"))

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

# Чтение всей таблицы
cursor.execute("SELECT * FROM Users")
results = cursor.fetchall()
for row in results:
    print(row)
print()  # Пустая строка

# Чтение выборочных полей
cursor.execute("SELECT username, balance FROM Users")
results = cursor.fetchall()
for row in results:
    print(row)
print()  # Пустая строка

# Изменение balance у каждой 2-й записи начиная с 1-й и вывод получившейся таблицы
# for i in range(1, 11):
#     if i % 2 != 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

cursor.execute("SELECT username, balance FROM Users")
results = cursor.fetchall()
for row in results:
    print(row)
print()  # Пустая строка

# Удаление каждой 3-й записи начиная с 1-й и вывод получившейся таблицы
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

cursor.execute("SELECT * FROM Users")
results = cursor.fetchall()
for row in results:
    print(row)
print()  # Пустая строка

# Вывод строк из базы с фильтрацией по возрасту "age != 60"
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", ("60",))

results = cursor.fetchall()
for row in results:
    print(row)
print()  # Пустая строка

# Вывод в консоль согласно задаче
for row in results:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

connection.commit()
connection.close()
