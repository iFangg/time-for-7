import os
import sys

# this gets rid of the stupid module not found error
sys.path.append(os.path.join(os.path.dirname('/Users/ifang/Documents/Projects/time-for-7/classes')))
from classes import event

from icalevents.icalevents import events
# from icalevents.icalparser import Event, Attendee


""" 
icalevents Event class:
    uid:            str
    summary:        str                             | None 
    description:    str                             | None 
    start:          datetime                        | None 
    end:            datetime                        | None 
    all_day:        bool 
    transparent:    bool 
    recurring:      bool 
    location:       str                             | None 
    private:        bool 
    created:        datetime                        | None 
    last_modified:  datetime                        | None 
    sequence:       str                             | None 
    recurrence_id:  datetime    | date              | None 
    attendee:       Attendee    | list[Attendee]    | None 
    organizer:      str                             | None 
    categories:     list[str | None] 
    floating:       bool 
    status:         str                             | None 
    url:            str                             | None 
    component:      Component                       | None 
"""


def grabCalendar(url: str, userId: str, isApple: bool = False) -> list[event.Event]:
    calEvents = events(url, fix_apple=isApple)
    
    return [
        event.Event(
            e.uid,
            e.summary,
            e.start,
            [userId],
            e.recurring,
            max(e.end - e.start, 0)
        ) for e in calEvents
    ]

# figure out how to update calendars
def updateCalendar(): pass

