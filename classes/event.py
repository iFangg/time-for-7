import uuid

class Event:
    def __init__(self, title, date, isRecurring = False, duration = 0, hasDetailsHidden = True):
        self._id = uuid.uuid4()
        self.title = title
        self.date = date
        self.isRecurring = isRecurring
        self.duration = duration
        self.hasDetailsHidden = hasDetailsHidden
    
    @property
    def id(self):
        return self._id
    