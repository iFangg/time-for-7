from user import User
from datetime import datetime

class Event:
    def __init__(self, 
                    uid: str,
                    title: str,
                    date: datetime,
                    attendees: list[User] = [],
                    isRecurring: bool = False,
                    duration: int = 0,
                    hasDetailsHidden: bool = True
                ):
        self.uid = uid
        self.title = title
        self.date = date
        self.attendees = attendees
        self.isRecurring = isRecurring
        self.duration = duration
        self.hasDetailsHidden = hasDetailsHidden
    
    # @property
    # def id(self):
    #     return self._id
