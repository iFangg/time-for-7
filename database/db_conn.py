import sqlite3

def db_connect():
    try:
        conn = sqlite3.connect("init.db")
        c = conn.cursor()

        return c
    except:
        raise SystemError("Unable to connect to db, check logs")
