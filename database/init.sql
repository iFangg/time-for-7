-- can use sqlite3 database/init.db < database/init.sql

CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL                          -- limit to 250 characters
);

CREATE TABLE IF NOT EXISTS Events (
    id INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,                            -- limit to 100 characters
    Duration REAL NOT NULL,
    Date NUMERIC NOT NULL,
    isRecurring NUMERIC NOT NULL DEFAULT 0,         -- boolean
    hasDetailsHidden NUMERIC NOT NULL DEFAULT 1     -- boolean
);

CREATE TABLE IF NOT EXISTS EventAttendees (
    eventId INTEGER,
    userId INTEGER,
    FOREIGN KEY(eventId) REFERENCES Events(id),
    FOREIGN KEY(userId) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS EventRecurrance (
    eventId INTEGER,
    startDate NUMERIC NOT NULL,
    endDate NUMERIC NULL,
    recurranceRule TEXT NULL,
    Interval INTEGER NOT NULL DEFAULT 1,
    Count INTEGER NOT NULL DEFAULT 1,
    byMonth TEXT NULL,
    byDay TEXT NULL,
    byYearDay TEXT NULL,
    FOREIGN KEY(eventId) REFERENCES Events(id)
);
