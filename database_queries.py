import sqlite3

# Enabled DB
db = sqlite3.connect('resources/database.db', check_same_thread=False)
sql = db.cursor()

def user_reg(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"SELECT id FROM users WHERE id = {user_id}")

    if sql.fetchone() is None:
        sql.execute("INSERT INTO users (id) VALUES (?)", (user_id,))
        db.commit()

        return 1

    return 0

def user_status(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"SELECT status FROM users WHERE id = {user_id}")
    return sql.fetchone()[0]

def user_info(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return sql.fetchone()

def admin(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"UPDATE users SET status = 2 WHERE id = {user_id}")
    db.commit()

def arbitr(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"UPDATE users SET status = 1 WHERE id = {user_id}")
    db.commit()
