import sqlite3

def create_database():
    con = None
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        );
        """)

        con.commit()
        print("Database created successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        if con is not None:
            con.close()

create_database()
