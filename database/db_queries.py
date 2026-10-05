import sqlite3
import database.db_adapters as dba
from database.db_conn import db_connect

cur = db_connect()

def getEvents():
    res = cur.execute("""
                        SELECT e.* 
                        FROM Events e 
                        INNER JOIN EventRecurrance er
                            ON er.eventId = e.id
                    """)

    events = res.fetchall()
    print(f"Events: {events}")
    
    return events

def getUsers():
    res = cur.execute("SELECT * FROM Users")

    users = res.fetchall()
    print(f"Users: {res}")

    return users

cur.close()
