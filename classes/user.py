class User:
    def __init__(self, name):
        self._id = ''
        self.name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @id.deleter
    def id(self):
        del self._id
        
    def print(self):
        print(f"""
              USER ID: {self._id}\n
              USER NAME: {self.name}
              """)