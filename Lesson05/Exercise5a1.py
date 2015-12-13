# Create an arena for the mighty heroes from Exercise 5-2.
# The game starts with hero class selection.
# Then the game will generate a random monster.
# The monster has health points and can attack the hero, subtracting some amount of HP.
# The monster can have (or not) an affix that reduces damage taken from fire,
# ice or arcane magic.
# The main point of the game is to stay alive (hero HP > 0) and defeat the enemy.
# An example combat log is shown here:

# > Please select a hero:
# > warrior
# > The game is begun
# > Warrior. HP: 200, Mana: 100
# > You see the monster. He's horrifying and dangerous.
# > Warrior. HP: 200, Mana: 100
# > Monster. HP: 100
# > Please select an action:
# > hammer_attack
# > Hit! Monster. HP: 70
# > Monster strikes you. Warrior. HP: 210
# > Please select an action
# > hero info
# > Warrior. HP: 210, Mana: 90
# > Please select an action
# > fireball
# > Hit! Monster defeated!
# > You win!
