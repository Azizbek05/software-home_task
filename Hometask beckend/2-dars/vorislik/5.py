class TUPLAM_AB:
    def __init__(self, toplam_a, toplam_b):
        self.toplam_a = toplam_a
        self.toplam_b = toplam_b

    def chop_qilish(self):
        return self.toplam_a, self.toplam_b


class TUPLAM_AMALLARI(TUPLAM_AB):
    def __init__(self, tuplam):
        self.tuplam = tuplam

    def yangi_element_qoshish(self, element):
        self.tuplam += (element,)

    def element_ochirish(self, index):
        if 0 <= index < len(self.tuplam):
            self.tuplam = self.tuplam[:index] + self.tuplam[index+1:]

    def keshishma(self):
        return hash(self.tuplam)

    def birlashma(self):
        return "".join(str(x) for x in self.tuplam)

    def ayirma(self):
        return list(self.tuplam)


