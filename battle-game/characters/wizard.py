from character import Character
from gears.weapon import Weapon
from gears.armor import Armor

class Wizard(Character):
    def __init__(self, name:str, hp:float, weapon:Weapon, armor:Armor, spell:float, mana):
        Character.__init__(self, name, hp, weapon, armor)
    
        