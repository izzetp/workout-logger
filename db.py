import sqlite3

def create_table():
    conn = sqlite3.connect("workouts.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              type TEXT NOT NULL,
              duration INTEGER NOT NULL,
              date TEXT NOT NULL
     )
''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()