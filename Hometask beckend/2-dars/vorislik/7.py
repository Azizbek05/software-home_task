class Taxta:
    def __init__(self):
        self.taxta = [[' ' for _ in range(8)] for _ in range(8)]

    def koordinatga_kiritish(self, koordinata, belgi):
        sutunlar = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        sutun = sutunlar[koordinata[0]]
        satr = 8 - int(koordinata[1])
        self.taxta[satr][sutun] = belgi

    def chop_qilish(self):
        for satr in self.taxta:
            print('|' + '|'.join(satr) + '|')
            print('+' + '-'*17 + '+')

class Farzin(Taxta):
    def __init__(self):
        super().__init__()

    def uradigan_kataklarni_belgilash(self, koordinatalar):
        for koordinata in koordinatalar:
            sutunlar = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
            sutun = sutunlar[koordinata[0]]
            satr = 8 - int(koordinata[1])
            if self.taxta[satr][sutun] == ' ':
                self.taxta[satr][sutun] = '0'
            else:
                self.taxta[satr][sutun] = 'X'