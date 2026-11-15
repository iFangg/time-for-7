from classes.user import User
from datetime import datetime

class Event:
    def __init__(self, 
                    uid: str,
                    title: str,
                    date: datetime,
                    attendees: list[User] = [],
                    isRecurring: bool = False,
                    duration: int = 0,
                    hasDetailsHidden: bool = True,
                    serverId: int = 0
                ):
        self.uid = uid
        self.title = title
        self.date = date
        self.attendees = attendees
        self.isRecurring = isRecurring
        self.duration = duration
        self.hasDetailsHidden = hasDetailsHidden
        self.serverId = serverId
    
    # @property
    # def id(self):
    #     return self._id
