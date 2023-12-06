from gears.weapon import Weapon
from gears.armor import Armor
from characters.character import Character

axe = Weapon('axe', 20)
staff = Weapon('staff', 15)

iron_armor = Armor('iron_armor', 10)
leather_armor = Armor('leather_armor', 8)

john = Character('john', 200, axe, leather_armor)
jane = Character('jane', 180, staff, iron_armor)

john.attack(jane)
print(john.name, john.hp, "HP")
print(jane.name, jane.hp, "HP")
input("------------------")
jane.attack(john)
print("Results: ")
print(john.name, john.hp, "HP")
print(jane.name, jane.hp, "HP")
input("------------------")


# print(axe.name)
# print(leather_armor.name)