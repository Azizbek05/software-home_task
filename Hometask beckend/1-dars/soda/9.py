class Uch:
    def __init__(self, a):
        self.a = a

    def yigindisi(self):
        raqam1 = self.a // 100
        raqam2 = (self.a % 100) // 10
        raqam3 = self.a % 10
        
        add = raqam1 + raqam2 + raqam3
        return add
    
    def kopaytmasi(self):
        raqam1 = self.a // 100
        raqam2 = (self.a % 100) // 10
        raqam3 = self.a % 10

        mult = raqam1 * raqam2 * raqam3
        return mult
    
