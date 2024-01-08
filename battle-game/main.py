from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Spell
from characters.wizard import Wizard
from characters.barbarian import Barbarian
from battleground.arena import Arena

axe = Weapon('axe', 13)
staff = Weapon('staff', 10)
magic_orb = Spell('Magic Orb', 12, 10)

iron_armor = Armor('iron_armor', 10)
leather_armor = Armor('leather_armor', 8)

john = Wizard('john', 200, staff, leather_armor, magic_orb, 2 )
jane = Barbarian('jane', 180, axe, iron_armor)
#jane hp = 180+10 = 190  john hp = 200 + 8 = 2008
#jane damage = 13 john atack damage = 10 john spell damage = 12

first_fight = Arena(john, jane)

first_fight.fight()

# john.attack(jane)
# input("------------------")
# jane.attack(john)

# input("------------------")
