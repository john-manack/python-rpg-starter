class Hero:
    def __init__(self):
        self.health = 10
        self.power = 5
    
    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.health
        print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")

class Goblin:
    def __init__(self):
        self.health = 6
        self.power = 2
    
    def attack(self, enemy):
        # Goblin attacks hero
        self.health -= enemy.health
        print("The goblin does %d damage to you." % self.power)
        if enemy.health <= 0:
            print("You are dead.")

hero = Hero()
goblin = Goblin()

hero.attack(goblin)
goblin.attack(hero)