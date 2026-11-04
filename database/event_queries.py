import sqlite3
import logging
from database.db_conn import db_connect
from classes.event import Event


logger = logging.getLogger('discord')


def getEvents():
    cur = db_connect()
    query = (
        """
            SELECT e.* 
            FROM Events e 
            INNER JOIN EventRecurrance er
                ON er.eventId = e.id
        """
    )
            
    try:
        res = cur.execute(query)

        events = res.fetchall()
        print(f"Events: {events}")
        logger.info("Events, Event Recurrance tables queried")
        
        # TODO: format before returning
        return events
    except (Exception) as e:
        raise Exception("Unable to get events, check logs")
    finally:
        cur.close()

def checkEventExists(eventId: int):
    cur = db_connect()
    query = "SELECT id FROM EVENTS WHERE id = ?"
    
    try:
        cur.execute(query, (eventId))

        res = cur.fetchall()
        print("search events by id: ", res)
        
        return True if len(res) > 0 else False
    except (Exception) as e:
        logger.error(f"Failed to check if event exists: {e}")
    finally:
        cur.close()


def upsertEvent(event: Event):
    cur = db_connect()
    upsert_inputs = {
        "id": event.id(),
        "title": event.title,
        "duration": event.duration,
        "date": event.date,
        "isRecurring": event.isRecurring,
        "hasDetailsHidden": event.hasDetailsHidden
    }

    upsert_event_query = (
        """
            INSERT INTO EVENTS(id, Title, Duration, Date, isRecurring, hasDetailsHidden)
            VALUES (:id, :title, :duration, :date, :isRecurring, :hasDetailsHidden)
                ON CONFLICT(id) 
                DO UPDATE SET
                    Title = :title,
                    Duration = :duration,
                    Date = :date,
                    isRecurring = :isRecurring,
                    hasDetailsHidden = :hasDetailsHidden
        """
    )

    try:
        cur.execute(upsert_event_query, upsert_inputs)
    except (Exception) as e:
        logger.error(f"Failed to update/insert event: {e}")
    finally:
        cur.close()

def addUserToEvent(eventId: int, userId: str):
    pass
    

