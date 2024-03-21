class Matn:
    def __init__(self, matn):
        self.matn = matn

    def oqish(self):
        return self.matn

    def saqlash(self, matn):
        self.matn = matn

    def chop_qilish(self):
        return self.matn


class Shifrlash(Matn):
    def __init__(self, matn):
        super().__init__(matn)

    def shifrlash(self, surishlar):
        alfavit = 'abcdefghijklmnopqrstuvwxyz'
        shifrlangan_matn = ''
        for i, harf in enumerate(self.matn):
            surish = surishlar[i % len(surishlar)]
            index = alfavit.index(harf)
            index = (index + surish) % len(alfavit)
            shifrlangan_matn += alfavit[index]
        return shifrlangan_matn


