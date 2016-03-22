from time import sleep
from random import randint

class Boxer:
    def __init__(self, name, health, strength, speed, dodge):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed
        self.dodge = dodge

    def hit(self, opponent):
        strength = self.strength
        opponent.health = opponent.health - strength 

def fight(boxer1, boxer2):
        while boxer1.health >= 0 or boxer2.health > 0 :
            sleep(1)
            speed = randint(0,101)
            dodge = randint(0,101)
            if speed < boxer1.speed and dodge < (100 - boxer2.dodge):
                boxer1.hit(boxer2)
            if speed < boxer2.speed and dodge < (100 - boxer1.dodge):
                boxer2.hit(boxer1)
            
            print(str(boxer1.health) +" " + str(boxer2.health))
        
b1 = Boxer("Boxer1", 100, 25, 70, 60)
b2 = Boxer("Boxer2", 100, 20, 80, 70)
fight(b1,b2)