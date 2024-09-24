import Warrior as w

class Army:
    def __init__(self, name = 'army'):
        self.members = []
        self.name = name
    def add_members(self, max_members: int, *figthers: object):
        for figther in figthers:
            if len(self.members) < max_members and isinstance(figther, w.Warrior):
                self.members.append(figther)
    def __add__(self, obj: int):
        for el in self.members:
            el += obj
    def __mul__(self, obj: int):
        for el in self.members:
            el *= obj