from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Spell 
from printtools.boxprint import Printbox
class Wizard(Character):
    
    def __init__(self, name:str, hp:float, weapon:Weapon, armor:Armor, spell:Spell, mana:float):
        Character.__init__(self, name, hp, weapon, armor)
        self.spell = spell
        self.mana = mana
        
    def attack(self, other):
        
        Printbox.print_box("Choose between attacking (press 1) or casting a spell (press 2): ")
        attk = input()
        if attk == '2':
            if self.mana >= self.spell.mana:
                other.hp =  round ( other.hp - self.spell.damage * ( 1 - other.armor.defense ), 2 )
                self.mana = self.mana - self.spell.mana
                Printbox.print_box(f"{self.name} has attacked {other.name} with the spell \"{self.spell.name}\"")
                Printbox.print_box(f"{other.name}'s hp = {other.hp} and {self.name}'s mana is now {self.mana}")
            else: 
                Printbox.print_box(f"The wizard does not have enough mana to cast a spell, {self.name} will launch a normal attack.")
                super().attack(other)         
                
        elif attk == '1':
            super().attack(other)
        else:
            self.attack(other)   
                  
    def summary(self):
        summary = f"{self.name} hp : {self.hp} \n{self.name} mana : {self.mana}"
        return summary
            
        
    
        