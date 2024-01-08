from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor

class Barbarian(Character):
    def __init__(self, name:str, hp:float, weapon:Weapon, armor:Armor):
        Character.__init__(self, name, hp, weapon, armor)
    
    def attack(self, other): 
        print(f'{self.name} is a barbarian, {self.name} will attack twice ')
        other.hp = other.hp + other.armor.defense - self.weapon.damage
        print(f"{self.name} has attacked once, {other.name}'s hp = {other.hp}")
        other.hp = other.hp + other.armor.defense - self.weapon.damage
        print(f"{self.name} has attacked again, {other.name}'s hp = {other.hp}")
    
