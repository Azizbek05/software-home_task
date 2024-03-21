class SATR:
    def __init__(self, satr):
        self.satr = satr

    def chop_qilish(self):
        return self.satr

class ARIFM_AMAL(SATR):
    def hisoblash(self):
        a, amal, b = self.satr.split()
        a = float(a)
        b = float(b)

        if amal == '+':
            return a + b
        elif amal == '-':
            return a - b
        elif amal == '*':
            return a * b
        elif amal == '/':
            if b == 0:
                return "Nolga bo'lish mumkin emas"
            return a / b
        else:
            return "Noto'g'ri amal"


