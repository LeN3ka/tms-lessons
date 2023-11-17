import sqlite3


with sqlite3.connect('SQLite.db') as connection:
    all_users = connection.execute('SELECT * FROM user')
    for user in all_users.fetchall():
         print(user)
    min_age = int(input("Введите минимальный возраст человека: "))
    user = connection.execute(
        'SELECT * FROM user WHERE age >= ?;',
        (min_age,))
    for user in user.fetchall():
        print(user)
