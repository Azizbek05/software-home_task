class KOP_HAD:
    def __init__(self, k, koef):
        self.k = k
        self.koef = koef

    def qiymat_olish(self, x):
        result = 0
        for i, coef in enumerate(self.koef):
            result += coef * (x ** (i+1))
        return result

    def chop_qilish(self):
        print("Koeffitsientlar:", self.koef)


class CHEBISHEV(KOP_HAD):
    def __init__(self, k, a, b):
        self.a = a
        self.b = b
        koef = self.chebishev_koeffisientlari(k)
        super().__init__(k, koef)

    def chebishev_koeffisientlari(self, k):
        koef = [0] * k
        koef[0] = 1
        koef[1] = self.b
        for i in range(2, k):
            koef[i] = 2 * self.b * koef[i-1] - koef[i-2]
        return koef

    def kophad_hisoblash(self, x):
        normalized_x = (2 * x - (self.a + self.b)) / (self.b - self.a)
        return super().qiymat_olish(normalized_x)

