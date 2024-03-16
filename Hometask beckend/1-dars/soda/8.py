class Tortburchak:
    def __init__(self, x1, x2,x3,x4, y1, y2,y3, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def yuzi(self):
        return ((self.x1*self.y2)
                +(self.x2*self.y3)
                +(self.x3*self.y4)
                +(self.x4*self.y1)
                +(self.x2*self.y1)
                +(self.x3*self.y2)
                +(self.x4*self.y3)
                +(self.x1*self.y4)
                *0.5)
    
