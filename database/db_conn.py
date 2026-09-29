import cs50
import sqlite3
import logging
from pathlib import Path
import os

DATABASE_ROOT = Path(__file__).parent
DATABASE_INIT_SQL = DATABASE_ROOT / "init.sql"
DATABASE_FILE = DATABASE_ROOT / "init.db"

def db_connect(logger: logging):
    try:
        logger.info("Establishing db connection...")
        # test = cs50.SQL("sqlite:///./database/init.db")
        
        conn = sqlite3.connect("./database/init.db")
        c = conn.cursor()
        
        if os.stat(DATABASE_FILE).st_size == 0:
            logger.info("Database empty, initialising db...")
            with open(DATABASE_INIT_SQL) as f:
                c.executescript(DATABASE_INIT_SQL)
            
        
        res = c.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")

        print("tables: ", res.fetchall())

        return c
    except (sqlite3.OperationalError, sqlite3.DatabaseError, RuntimeError) as e:
        logger.error(f"Failed to connect to db: {e}")
        raise SystemError("Unable to connect to db, check logs")
