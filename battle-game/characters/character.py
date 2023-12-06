class Character:
    def __init__ (self, name:str, hp:float, weapon, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
    def attack(self, other):
        self.hp = self.hp + self.armor.defense - other.weapon.damage
        return self.hp
        
        