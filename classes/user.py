import uuid

class User:
    def __init__(self, name):
        self._id = uuid.uuid4()
        self.name = name

    @property
    def id(self):
        return self._id
    