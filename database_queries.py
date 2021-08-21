import sqlite3

# Enabled DB
db = sqlite3.connect('resources/database.db', check_same_thread=False)
sql = db.cursor()

def user_reg(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"SELECT id_user FROM users WHERE id_user = '{user_id}'")

    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (id)", (user_id))
        db.commit()

        return 1

    return 0
