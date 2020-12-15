class Hero:
    def __init__(self, health=10, power=5):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")
            
    def alive(self):
        self.health > 0        

class Goblin:
    def __init__(self, health=6, power=2):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if enemy.health <= 0:
            print("You are dead.")
            
    def alive(self):
        self.health > 0

hero = Hero()
goblin = Goblin()

hero.attack(goblin)
goblin.attack(hero)

while goblin.alive() and hero.alive():
    print("You have %d health and %d power." % (hero_health, hero_power))
    print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()