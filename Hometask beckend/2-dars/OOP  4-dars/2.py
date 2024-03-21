class Kompleks:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def qoshish(self, other):
        real_jami = self.real + other.real
        imag_jami = self.imag + other.imag
        return Kompleks(real_jami, imag_jami)

    def ayrish(self, other):
        real_ayirma = self.real - other.real
        imag_ayirma = self.imag - other.imag
        return Kompleks(real_ayirma, imag_ayirma)

    def kopaytirish(self, other):
        real_kopaytirish = self.real * other.real - self.imag * other.imag
        imag_kopaytirish = self.real * other.imag + self.imag * other.real
        return Kompleks(real_kopaytirish, imag_kopaytirish)

    def bolish(self, other):
        real_bolish = (self.real * other.real + self.imag * other.imag) / (other.real**2 + other.imag**2)
        imag_bolish = (self.imag * other.real - self.real * other.imag) / (other.real**2 + other.imag**2)
        return Kompleks(real_bolish, imag_bolish)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

kompleks1 = Kompleks(3, 4)
kompleks2 = Kompleks(5, 2)

print("1. Kompleks son:", kompleks1)
print("2. Kompleks son:", kompleks2)
print("Qo'shish:", kompleks1.qoshish(kompleks2))
print("Ayrish:", kompleks1.ayrish(kompleks2))
print("Ko'paytirish:", kompleks1.kopaytirish(kompleks2))
print("Bo'lish:", kompleks1.bolish(kompleks2))
