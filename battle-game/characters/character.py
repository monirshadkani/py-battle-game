from gears.weapon import Weapon
from gears.armor import Armor

class Character:
    def __init__ (self, name:str, hp:float, weapon:Weapon, armor:Armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
    def attack(self, other):
        other.hp = other.hp + other.armor.defense - self.weapon.damage        
        print( f'{self.name} has attacked {other.name}, {self.name} hp: {self.hp} and {other.name} hp: {other.hp}')
        return other.hp

    def summary(self):    
        summary = f"{self.name} hp : {self.hp}\n{self.name} armor defense : {self.armor.defense} \n"
        return summary