from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from printtools.boxprint import Printbox

class Barbarian(Character):
    def __init__(self, name:str, hp:float, weapon:Weapon, armor:Armor):
        Character.__init__(self, name, hp, weapon, armor)
    
    def attack(self, other:Character): 
        Printbox.print_box(f'{self.name} is a barbarian, {self.name} will attack twice ')
        super().attack(other)
        if other.checkLife() :
            super().attack(other)
    
