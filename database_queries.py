def user_reg(**kwargs):
    sql.execute(f"SELECT id_user FROM users WHERE id_user = '{user_id}'")

    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (id)", (user_id))
        db.commit()

        log.info(f'User {user_id} was registered')
