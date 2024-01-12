from gears.weapon import Weapon
from gears.armor import Armor
from printtools.boxprint import Printbox

class Character:
    def __init__ (self, name:str, hp:float, weapon:Weapon, armor:Armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
    def attack(self, other):
        other.hp = round ( other.hp - self.weapon.damage * ( 1 - other.armor.defense ), 2 )    
        Printbox.print_box( f'{self.name} has attacked {other.name}, {self.name} hp: {self.hp} and {other.name} hp: {other.hp}')
        
    def summary(self):    
        summary = f"{self.name} hp : {self.hp}"
        return summary
    
    def checkLife(self):
        if self.hp > 0 :
            return True
        return False