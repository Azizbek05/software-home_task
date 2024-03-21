import math

class VEKTOR_XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class VEKTOR_XY_AMAL(VEKTOR_XY):
    def __init__(self, vektor1, vektor2):
        self.vektor1 = vektor1
        self.vektor2 = vektor2

    def qosish(self):
        x = self.vektor1.x + self.vektor2.x
        y = self.vektor1.y + self.vektor2.y
        return VEKTOR_XY(x, y)

    def ayirish(self):
        x = self.vektor1.x - self.vektor2.x
        y = self.vektor1.y - self.vektor2.y
        return VEKTOR_XY(x, y)

    def skalyar_kopaytma(self):
        return self.vektor1.x * self.vektor2.x + self.vektor1.y * self.vektor2.y

    def uzunlik(self):
        return math.sqrt(self.vektor1.x ** 2 + self.vektor1.y ** 2)

    def i(self):
        return math.atan2(self.vektor1.y, self.vektor1.x) * 180 / math.pi

vektor1 = VEKTOR_XY(3, 4)
vektor2 = VEKTOR_XY(5, 6)

amal = VEKTOR_XY_AMAL(vektor1, vektor2)
