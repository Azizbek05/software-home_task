class Massiv:
    def __init__(self, massiv):
        self.massiv = massiv

    def musbat(self):
        manfiy = [i for i in self.massiv if i < 0]
        musbat = [i for i in self.massiv if i > 0]

        self.massiv = manfiy + musbat  
        return self.massiv  

massiv = [10, 23, -43, 32, -14, -12]
obj = Massiv(massiv)

print(obj.musbat())
