import os
os.system('cls')

class Vechile:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Full(Vechile):
    def __init__(self, brand, speed, mountain):
        super().__init__(brand, speed)
        self.mountanin = mountain

sip = Full("Bmw", 50, )