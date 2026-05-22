from models.db import get_db

def get_posts():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM posts ORDER BY idx DESC")
    data = cur.fetchall()

    conn.close()
    return data


def insert_post(title, content, writer):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO posts(title, content, writer) VALUES(%s,%s,%s)",
        (title, content, writer)
    )

    conn.commit()
    conn.close()


def delete_post(idx):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM posts WHERE idx=%s", (idx,))
    conn.commit()
    conn.close()


def get_post(idx):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM posts WHERE idx=%s", (idx,))
    data = cur.fetchone()

    conn.close()
    return data


def update_post(idx, title, content):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "UPDATE posts SET title=%s, content=%s WHERE idx=%s",
        (title, content, idx)
    )

    conn.commit()
    conn.close()