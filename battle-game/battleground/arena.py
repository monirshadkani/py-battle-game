from characters.character import Character

class Arena:
    def __init__(self, first_character: Character, second_character: Character):
        self.first_character = first_character
        self.second_character = second_character
        
    def fight(self):
        round = 1
        while self.first_character.hp > 0 or self.first_character.hp > 0 :
            print(f"Round {round}: the battle has started, {self.first_character.name} will attack {self.second_character.name} first:") 
            self.first_character.attack(self.second_character)
            self.second_character.attack(self.first_character)
            print(f"round {round} has ended, here is the summary:")
            
            print(f'{self.first_character.summary()} \n{self.second_character.summary()}')
            round += 1