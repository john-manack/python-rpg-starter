class Character:
    def __init__(self, name, health=0, power=0):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("%s does %d damage to the %s." % (self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("%s is dead" % enemy.name)
    
    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

hero = Character("Link", 10, 5)
goblin = Character("Zombie", 100, 8)

while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print("")
    print("What do you want to do?")
    print("1. fight %s" % goblin.name)
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