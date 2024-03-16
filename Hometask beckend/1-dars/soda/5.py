class Kordinata:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def masofa(self):
        return ((self.x2 - self.x1)*(self.y2 - self.y1)**0.5)
    
kordinata = Kordinata(5,5,3,6)

print(kordinata.masofa())