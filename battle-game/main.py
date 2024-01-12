from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Spell
from characters.wizard import Wizard
from characters.barbarian import Barbarian
from battleground.arena import Arena
from printtools.boxprint import Printbox
from characters.character import Character

axe = Weapon('axe', 20)
club = Weapon('club', 25)
staff = Weapon('staff', 10)
wand = Weapon('wand', 15)

magic_orb = Spell('Magic Orb', 34, 10)
wind_bullet = Spell('Wind bullet', 20, 5)

iron_armor = Armor('iron armor', 0.3)
leather_armor = Armor('leather armor', 0.2)
dragon_armor = Armor('dragon armor', 0.5)
bear_skin = Armor('bear skin', 0.1)


great_oracle = Wizard('The Great Oracle', 100, staff, iron_armor, magic_orb, 20 )
arch_mage = Wizard('The Arch Mage', 80, wand, dragon_armor, wind_bullet, 40 )

list_wizard = [great_oracle, arch_mage] #To be able to do wizard choice

arthur_decapitator = Barbarian('Arthur the Decapitator', 100, axe, leather_armor)
attila_crazy = Barbarian('Attila the Crazy', 100, club, bear_skin)

list_barbarian = [arthur_decapitator, attila_crazy] #To be able to do barbarian choice

Printbox.print_box(f'Please choose the Wizard that will fight between {great_oracle.name} (press 1) or {arch_mage.name} (press 2):')
first_player = list_wizard[Printbox.player_choice()]

Printbox.print_box(f'Then choose the barbarian that will fight {first_player.name} between {arthur_decapitator.name} (press 1) or {attila_crazy.name} (press 2):')
second_player = list_barbarian[Printbox.player_choice()]

first_arena = Arena(first_player, second_player)

first_arena.fight()


    
