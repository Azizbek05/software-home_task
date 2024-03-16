class Uchburchak:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def uchburchak_yuzi(self):
        return (0.5 *(self.x1 *(self.y2 - self.y3) + self.x2 *(self.y3 - self.y1) + self.x3 *(self.y1 - self.y2)))
        
uch = Uchburchak(1,2,3,10,5,6)

print(uch.uchburchak_yuzi())