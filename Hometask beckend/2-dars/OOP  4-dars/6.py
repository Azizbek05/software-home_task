class KITOB:
    def __init__(self, nomi, muallif, yil):
        self.nomi = nomi
        self.muallif = muallif
        self.yil = yil

class UY_KUTUBXONASI:
    def __init__(self):
        self.kitoblar = []

    def kitob_izlash(self, parametr):
        natija = []
        for kitob in self.kitoblar:
            if parametr in [kitob.nomi, kitob.muallif, str(kitob.yil)]:
                natija.append(kitob)
        return natija

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def kitob_ochirish(self, kitob):
        self.kitoblar.remove(kitob)

