import sqlite3

# Create SQLite database and table structure
conn = sqlite3.connect('tennis.db')
cursor = conn.cursor()

# Create table for matches
cursor.execute('''
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team1 TEXT NOT NULL,
    team2 TEXT NOT NULL,
    date TEXT NOT NULL,
    winner TEXT
)
''')

conn.commit()
conn.close()
