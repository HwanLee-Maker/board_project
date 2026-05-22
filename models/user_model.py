from models.db import get_db

def check_user(user_id, password):
    conn = get_db()
    cur = conn.cursor()

    sql = "SELECT * FROM users WHERE id=%s AND password=%s"
    cur.execute(sql, (user_id, password))
    user = cur.fetchone()

    conn.close()
    return user