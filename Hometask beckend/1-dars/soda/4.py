import math as m
class Doira:
    def __init__(self, s):
        self.s = s

    def r_ropish(self):
        return f"{(self.s/m.pi)**0.5}"
    
uz = Doira(10)

print(uz.r_ropish())