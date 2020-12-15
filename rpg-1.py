class Character:
    def __init__(self, health=0, power=0):
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

class Hero(Character):
    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
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

hero = Hero(10, 5)
goblin = Goblin(6, 2)

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