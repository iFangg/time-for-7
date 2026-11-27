# Scheduling discord bot for friend groups

## Packages needed:
- dotenv
- discord
- icalendar
- icalevents


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

# Notes
- assume working week start is monday

# Commands
- creating an event flow:
    - check if event exists
    - confirm with user if they would like to modify that event?
        - end if no
        - modify if yes
    - create new event if not exists 
