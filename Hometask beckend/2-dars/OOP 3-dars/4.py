class Massiv:
    def __init__(self, massiv):
        self.massiv = massiv

    def soni(self):
        son_manfiy = []
        for i in self.massiv:
            if i < 0:
                son_manfiy.append(i)
        son_musbat = []
        for i in self.massiv:
            if i > 0:
                son_musbat.append(i)

        son_musbat = len(son_musbat)
        son_manfiy = len(son_manfiy)

        return f"{son_musbat} ta musbat son {son_manfiy} ta manfiy son"
    
massiv = [10, 23, -43, 32, -14, -12]

obj = Massiv(massiv)

print(obj.soni())