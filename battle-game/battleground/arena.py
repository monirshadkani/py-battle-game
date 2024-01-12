from characters.character import Character
from printtools.boxprint import Printbox

class Arena:
    def __init__(self, first_character: Character, second_character: Character):
        self.first_character = first_character
        self.second_character = second_character
        
    def fight(self):
        round = 1
        while self.first_character.checkLife() and self.second_character.checkLife():
            Printbox.print_box(f"Round {round}: the battle has started, {self.first_character.name} will attack {self.second_character.name} first:") 
            self.first_character.attack(self.second_character)
            input("\n")
            
            if self.second_character.checkLife():
                self.second_character.attack(self.first_character)
                input("\n")

            if self.first_character.checkLife() and self.second_character.checkLife():
                self.minisummary(round)
                round += 1 
            
        self.bigsummary(round)
            
    def minisummary(self, round_number):
        Printbox.print_box(f"Round {round_number} has ended, here is the summary:")
        if(self.first_character.hp == self.second_character.hp):
            Printbox.print_box(f"The battle is intense! {self.first_character.name} ({self.first_character.hp} hp) and {self.second_character.name} ({self.second_character.hp} hp) have the same hp!")
        else:
            character_more_hp = self.first_character
            character_less_hp = self.second_character
            delta_hp = self.first_character.hp - self.second_character.hp
            
            if self.first_character.hp < self.second_character.hp :
                character_more_hp = self.second_character
                character_less_hp = self.first_character
                delta_hp = self.second_character.hp - self.first_character.hp
                
            delta_hp = round(delta_hp, 2)
            Printbox.print_box(f"{character_more_hp.name} ({character_more_hp.hp} hp) has the advantage of the fight! This character has {delta_hp} more hp than {character_less_hp.name} ({character_less_hp.hp} hp)!")
    
    def bigsummary(self, round_number):
        winner = self.first_character
        loser = self.second_character
        if self.second_character.checkLife():
            winner = self.second_character
            loser = self.first_character
            
        Printbox.print_box (f"{loser.name} has died, {winner.name} has won the battle!")
        Printbox.print_box(f"The game is finished, it lasted {round_number} rounds! {winner.summary()} {loser.summary()}")
            
               
    
    