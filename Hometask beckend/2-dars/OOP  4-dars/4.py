import math

class VEKTOR2_3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def qoshish(self, other):
        return VEKTOR2_3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def ayrish(self, other):
        return VEKTOR2_3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def skalyar_kopaytma(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def uzunlik(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def burchak_kosinus(self, other):
        scalar_product = self.skalyar_kopaytma(other)
        magnitude_product = self.uzunlik() * other.uzunlik()
        return scalar_product / magnitude_product

