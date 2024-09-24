import Warrior as w

class Defender(w.Warrior): 
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2
    def get_damage(self, enemy_attack):
        if enemy_attack > self.defense:
            enemy_attack -= self.defense
            self.health -= enemy_attack 
            return enemy_attack
        else: 
            return 0
    def special_char_desc(self, add_comma = True):
        res = f'{str(self.defense)} defense'
        if add_comma:
            return ', ' + res
        else:
            return res