import sqlite3
import logging
import database.db_adapters as dba
from database.db_conn import db_connect


logger = logging.getLogger('discord')

def getEvents():
    cur = db_connect()
    query = """
                SELECT e.* 
                FROM Events e 
                INNER JOIN EventRecurrance er
                    ON er.eventId = e.id
            """
            
    try:
        res = cur.execute(query)

        events = res.fetchall()
        print(f"Events: {events}")
        logger.info("Events, Event Recurrance tables queried")
        
        return events
    except (Exception) as e:
        raise Exception("Unable to get events, check logs")
    finally:
        cur.close()

