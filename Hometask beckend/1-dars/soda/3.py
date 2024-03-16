import math as m

class Aylana:
    def __init__(self, r):
        self.r = r 

    def aylana_y(self):
        return f"{2*m.pi*self.r}"
    
    def doira_y(self):
        return f"{m.pi * (self.r**2)}"
    
    def __str__(self):
        return f"Aylananing uzunligi: {self.aylana_y()}, Doiraning yuzi: {self.doira_y()}"
    

r = Aylana(5)
print(r)