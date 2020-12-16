import random
class Character:
    def __init__(self, name, health=0, power=0):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
    
    def print_status(self):
        print("%s has %d health and %d power" % (self.health, self.power))

class Hero(Character):
    def attack(self, enemy):
        # Hero attacks goblin
        rand_num1 = random.randrange(1,10)
        if rand_num1 <= 2:
            enemy.health -= (self.power * 2)
        else:
            enemy.health -= self.power
        if rand_num1 <= 2:
            print("You do %d damage to the goblin." % (self.power * 2))
        else:
            print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Goblin(Character):
    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if enemy.health <= 0:
            print("You are dead.")

    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

hero = Hero("Link", 10, 5)
goblin = Goblin("Mr. Goblin", 6, 2)

while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print("")
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()
    if user_input == "1":
        hero.attack(goblin)
    elif user_input == "2":
        pass
    elif user_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)
    
    if goblin.alive():
        goblin.attack(hero)