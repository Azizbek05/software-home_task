class Massiv:
    def __init__(self, massiv):
        self.massiv = massiv

    def max_index(self):
        inde = self.massiv.index(max(self.massiv))

        return inde
    
massiv = [1,5,16,25,18]
obj = Massiv(massiv)

print(obj.max_index())