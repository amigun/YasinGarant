import sqlite3, time

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
    sql.execute(f"SELECT status FROM users WHERE id = ?", (user_id,))
    return sql.fetchone()[0]

def user_info(**kwargs):
    user_id = list(kwargs.items())[0][1]
    try:
        sql.execute(f"SELECT * FROM users WHERE id = ?", (user_id,))
    except sqlite3.OperationalError:
        return 1
    return sql.fetchone()

def admin(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"UPDATE users SET status = 2 WHERE id = ?", (user_id,))
    db.commit()

def arbitr(**kwargs):
    user_id = list(kwargs.items())[0][1]
    sql.execute(f"UPDATE users SET status = 1 WHERE id = ?", (user_id,))
    db.commit()

def create_deal(**kwargs):
    sql.execute(f"INSERT INTO transactions (buyer, seller, condition, price, commission, time) VALUES (?, ?, ?, ?, ?, ?)", (kwargs['buyer'], kwargs['seller'], kwargs['condition'], kwargs['price'], kwargs['commission'], int(time.time())))
    db.commit()

def list_of_offers_of_deals_pending(**kwargs):
    sql.execute(f"SELECT id FROM transactions WHERE seller = ? AND status = 4", (kwargs['seller'],))
    return sql.fetchall()

def deal_info(**kwargs):
    sql.execute(f"SELECT * FROM transactions WHERE id = ?", (kwargs['id_deal'],))
    return sql.fetchone()
