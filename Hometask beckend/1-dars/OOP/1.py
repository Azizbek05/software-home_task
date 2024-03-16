class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
    def mod(self):
        return self.a % self.b
    
    def pow(self):
        return self.a ** self.b
    
    def max(self):
        if self.a > self.b:
            print(f"{self.a} max")

        else:
            print(f"{self.b} max")

    def min(self):
        if self.a < self.b:
            print(f"{self.a} min")
        else:
            print(f"{self.b} min")
        return 
        
    def orta(self):
        return (self.a + self.b)/2
    

    def geometric(self):
        return (self.a * self.b)**0.5