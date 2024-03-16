class Uchburchak:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def yuzi(self):
        return (self.a * self.b) / 2
        

    def perimetr(self):
        return self.a + self.b + (self.a ** 2 + self.b ** 2) ** 0.5
        


num1 = Uchburchak(5, 6)

print(num1.perimetr())