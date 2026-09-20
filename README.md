# Scheduling discord bot for friend groups

## Research
- [discord.py](https://discordpy.readthedocs.io/en/stable/intro.html)
- [python calendar](https://docs.python.org/3/library/calendar.html)
- [google calendar python integration](https://developers.google.com/workspace/calendar/api/quickstart/python)
- [apple icalendar python](https://icalendar.readthedocs.io/en/stable/)
- [icalendar](https://icalendar.readthedocs.io/en/latest/how-to/usage.html)  - parsing and creating calendars
- [caldav python library](https://github.com/python-caldav/caldav)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) for pythobn
- [ical recurence structure](https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html)
- [ical validator](https://icalendar.org/validator.html)
- [sqlite types](https://www.sqlite.org/datatype3.html)


## Requirements
- can view shared calendar (optional)
- can add/remove events from shared calendar (optional)
- can connect to multiple calendars
- creates shared calendar for everyone to see
- polling sync for apple calendars
- live sync/push sync for google calendars
- shows upcoming scheduled events
    - shows who has rsvp’d
- calculates who is free on which day

# Tech stack
- python
- sqlite
- various APIs

# database tables

## users
- id (guid) pk
- name
## events 
- id pk
- title
- duration
- date
- isRecurring
- hasDetailsHidden
## event attendees
- event id
- user id
## event reccurance
- event id
- startDate
- endDate NULL
- recuranceRule (DAILY|WEEKLY|MONTHLY|YEARLY|CUSTOM)
- interval (when is the next time it occurs)
- count (how many times it recurs)
- byMonth (which months does it repeat on)
- byDay (which days does it repeat on)
- byYearDay (which days of the year e.g every 1st/100th day of the year)

# Notes
- assume working week start is monday
