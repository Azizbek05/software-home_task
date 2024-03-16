class Yigindi:
    def __init__(self, a):
        self.a = a

    def yigindi(self):
        all = 0
        for i in range(self.a+1):
            all += i
        return all
    
    def kopaytma(self):
        all = 1
        for i in range(1, self.a+1):
            all *= i
        return all

obj = Yigindi(5)

print(obj.yigindi())
print(obj.kopaytma())