import Warrior as w

class Vampire(w.Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50
    def healing(self, dealt_damage):
        self.health += dealt_damage * self.vampirism/100
    def deal_damage(self, victim):
        self.healing(super().deal_damage(victim))
    def special_char_desc(self, add_comma = True):
        res = f'{str(self.vampirism)}% vampirism'
        if add_comma:
            return ', ' + res
        else:
            return res