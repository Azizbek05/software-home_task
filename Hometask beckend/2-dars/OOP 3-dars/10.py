class Teskari:
    def __init__(self, a):
        self.a = a

    def teskari(self):
        revers = list(reversed(self.a))

        return revers 
    
my_list = [1,2,3,4,5,6,7,8,9,10]    
obj = Teskari(my_list)

print(obj.teskari())

