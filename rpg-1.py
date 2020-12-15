class Character:
    def __init__(self, health=0, power=0):
        self.health = health
        self.power = power

    def alive(self):
        self.health > 0

class Hero(Character):
    def __init__(self, health=10, power=5):
        super().__init__()
    
    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")
    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Goblin(Character):
    def __init__(self, health=10, power=5):
        super().__init__()
    
    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if enemy.health <= 0:
            print("You are dead.")
    
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

hero = Hero()
goblin = Goblin()

hero.attack(goblin)
goblin.attack(hero)

while goblin.alive() and hero.alive():
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()