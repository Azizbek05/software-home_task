class KO_PHAD:
    def __init__(self, daraja, *args):
        self.daraja = daraja
        self.koeffisientlar = args

    def qiymat(self, x):
        qiymat = 0
        for i, koeffisient in enumerate(self.koeffisientlar):
            qiymat += koeffisient * (x ** (self.daraja - i))
        return qiymat

    def tartib(self):
        return self.koeffisientlar[::-1]
