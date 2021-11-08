import sqlite3
from random import randint

connect = sqlite3.connect('baza.db')
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    cash BIGINT
)""")
connect.commit()



def reg():
    user_login = input('Logini kiriting: ')
    user_password = input('Parolni kiriting: ')


    cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login , user_password, 0))
        connect.commit()

        print('Siz ruyxatdan utingiz')
    else:
        print('bu akkaunt ruyxatdan utgan bowqa login tering !!!!!!!!!!!!!!!!!!!')


def delete_db():
    cur.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    connect.commit()
    print('udalit buldi')






def cazino():
    user_login = input('login: ')
    number = randint(1,2)
    cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cur.fetchone() is None:
        print('Bunaqa login hali yoq log in please ')
        reg()

    else:
        if number == 1:
            cur.execute(f"UPDATE users SET cash  = {1000} WHERE login = '{user_login}'")
            connect.commit()
            print('Yutuq')
        else:
            print('Game over')


def enter():
    for i in cur.execute('SELECT login, cash FROM users '):
        print(i)

def main():
    cazino()
    enter()

main()