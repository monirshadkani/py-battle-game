from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Spell 

class Wizard(Character):
    
    def __init__(self, name:str, hp:float, weapon:Weapon, armor:Armor, spell:Spell, mana:float):
        Character.__init__(self, name, hp, weapon, armor)
        self.spell = spell
        self.mana = mana
        
    def attack(self, other):
        
        print("Choose between attacking(press 1) or casting a spell (press 2): ")
        attk = input()
        if attk == '2':
            if self.mana >= self.spell.mana:
                other.hp = other.hp + other.armor.defense - self.spell.damage
                self.mana = self.mana - self.spell.mana
                print(f"{self.name} has attacked {other.name} with the spell \"{self.spell.name}\"")
                print(f"{other.name}'s hp = {other.hp} and {self.name}'s mana is now {self.mana}")
            else: 
                print(f"The wizard does not have enough mana to cast a spell, {self.name} will launch a normal attack.")
                super().attack(other)
                
        if attk == '1':
            super().attack(other)
            
    def summary(self):
        summary = f"{self.name} hp : {self.hp} \n{self.name} mana : {self.mana} \n{self.name} armor defense : {self.armor.defense}"
        return summary
            
        
    
        