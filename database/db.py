import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    url TEXT UNIQUE,
    source TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

def save_article(title, url, source):

    cursor.execute(
        "SELECT url FROM articles WHERE url=?",
        (url,)
    )

    exists = cursor.fetchone()

    if exists:
        print("Duplicate article skipped")
        return

    cursor.execute(
        "INSERT INTO articles (title, url, source) VALUES (?, ?, ?)",
        (title, url, source)
    )

    conn.commit()

    print("Article saved")

def get_today_articles():
    cursor.execute("""
        SELECT title FROM articles
        ORDER BY created_at DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    articles = [row[0] for row in rows]

    return articles