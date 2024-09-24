class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    def is_alive(self):
        return self.health > 0
    def get_damage(self, enemy_attack):
        self.health -= enemy_attack
        return enemy_attack
    def deal_damage(self, victim):
        return victim.get_damage(self.attack)
    def special_char_desc(self, add_comma = True):
        return f''
    def __str__(self):
        return f'{self.get_class()} Type, {self.health} health, {self.attack} damage{self.special_char_desc()}'
    def __add__(self, obj):
        if isinstance(obj, int) and obj > 0:
            self.health += obj
            self.attack += obj
        return self
    def __mul__(self, obj):
        if isinstance(obj, int) and obj > 0:
            self.health *= obj
            self.attack *= obj
        return self
    def get_class(self):
        return self.__class__.__name__