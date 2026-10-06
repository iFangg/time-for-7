import sqlite3
import logging
from classes import user
import database.db_adapters as dba
from database.db_conn import db_connect


logger = logging.getLogger('discord')

def getUsers():
    cur = db_connect()
    query = "SELECT * FROM Users"

    try:
        res = cur.execute(query)

        users = res.fetchall()
        print(f"Users: {users}")
        logger.info("Users table queried")

        # TODO: format before returning
        return users
    except (Exception) as e:
        logger.error(f"Error getting users: {e}")
        raise Exception("Unable to get users, check logs")
    finally:
        cur.close()

def registerUser(user: user.User):
    user.print()
    cur = db_connect()
    search_query = (
        """
            SELECT * 
            FROM Users
            WHERE id = ?
                AND Name = ?
            LIMIT 1
        """
    )
    
    insert_query = (
        """
            INSERT INTO Users 
            (id, Name)
            VALUES
            ?, ?
        """
    )
    
    try:
        res = cur.execute(search_query, (user._id, user.name))
        
        user_exists_fetch = res.fetchall()
        print(user_exists_fetch)
        
        if len(user_exists_fetch) > 0:
            logger.info("User already exsists, registration unsuccessful")
            return "USER ALREADY EXISTS"

        res = cur.execute(insert_query, (user._id, user.name))
        
        logger.info(f"User {user._id} - {user.name} inserted into table")
    except (Exception) as e:
        logger.error(f"Error registering user: {e}")
        raise Exception("Unable to register user, check logs")
    finally:
        cur.close()
