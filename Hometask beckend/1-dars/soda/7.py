class Qiymat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def arifmetik(self):
        return (self.a + self.b)/2
    
    def geametrik(self):
        return (self.a * self.b)**0.5
    
qiy = Qiymat(10, 15)

print(qiy.geametrik())