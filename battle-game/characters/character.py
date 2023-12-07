class Character:
    def __init__ (self, name:str, hp:float, weapon, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
    def attack(self, other):
        other.hp = other.hp + other.armor.defense - self.weapon.damage
        return other.hp

        