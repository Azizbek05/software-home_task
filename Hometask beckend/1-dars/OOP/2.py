class Uchburchak:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def yuzi(self):
        return self.a * self.b*self.c
    
    def peremetri(self):
        return self.a + self.b + self.c
    

    def guas(self):
        p = self.a + self.b + self.c
        p1 = p//2
        return 0.5 ** (p1 *(p1 - self.a) * (p1 - self.b) * (p1 - self.c))
    
    