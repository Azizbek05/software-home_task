class Masala:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        

    def maximum(self):
        if self.a > self.b:
            if self.a > self.c:
                return f"{self.a} eng katta son"
            elif self.a<self.c:
                return f"{self.c} eng katta son"
        
        elif self.b > self.a:
            if self.b > self.c:
                return f"{self.b} eng katta son"
            elif self.b<self.c:
                return f"{self.c} eng katta son"

        elif self.c > self.a:
            if self.c > self.b:
                return f"{self.c} eng katta son"
            elif self.c<self.b:
                return f"{self.b} eng katta son"
            

    def minimum(self):
        if self.a < self.b:
            if self.a < self.c:
                return f"{self.a} eng kichik son"
            elif self.a>self.c:
                return f"{self.c} eng kichik son"
        
        elif self.b < self.a:
            if self.b < self.c:
                return f"{self.b} eng kichik son"
            elif self.b>self.c:
                return f"{self.c} eng kichik son"
            
        elif self.c < self.a:
            if self.c < self.b:
                return f"{self.c} eng kichik son"
            elif self.c>self.b:
                return f"{self.b} eng kichik son"


obj = Masala(10,15,25)

print(obj.minimum())