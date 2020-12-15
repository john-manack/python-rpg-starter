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

hero = Hero()
goblin = Goblin()

hero.attack(goblin)