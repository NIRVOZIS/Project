import sqlite3 as sl


def get_add(login, password):
    r = 0
    con = sl.connect('DB\profile.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS profile(
    userid INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL);
    """)
    con.commit()

    cur.execute('SELECT*FROM profile')
    all_result = cur.fetchall()
    for row in all_result:
        if not row[0]:
            r += 1
        elif row[0]:
            r = row[0] + 1
    users = (r, login, password)
    cur.execute(f"""INSERT OR IGNORE INTO profile VALUES(?, ?, ?);""", users)
    print(f'Добавлен новый аккаунт!')
    con.commit()


def get_watch_db():
    try:
        con = sl.connect('DB\profile.db')
        cur = con.cursor()
        cur.execute("SELECT*FROM profile")
        all_result = cur.fetchall()
        print(f'Всего аккаунтов добавлено: {len(all_result)}')
        for row in all_result:
            print(f'ID: {row[0]} | LOGIN: {row[1]} | PASSWORD: {row[2]}')
    except sl.Error as err:
        print(f'Ошибка при работе с SQLite: {err}')
    finally:
        if con:
            con.close()
            print('Ваша База Данных закрыта, Спасибо за использование!')


def get_delete(userid):
    con = sl.connect('DB\profile.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM profile WHERE userid = {userid}")
    print(f'Аккаунт под ID {userid} был удален!')
    con.commit()
