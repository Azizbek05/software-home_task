class Masiv:
    def __init__(self, masiv):
        self.masiv = masiv

    
    def add_masiv(self):
        add = 0
        for n in range(self.masiv):
            add += n
        return add
    
    def sub_masiv(self):
        sub = 0
        for n in range(self.masiv):
            sub -= n
        return sub
    
    def mul_masiv(self):
        mul = 1
        for n in range(1,self.masiv+1):
            mul *= n
        return mul
    
    def div_masiv(self):
        div = 1
        for n in range(1,self.masiv+1):
            div /= n
        return div

obj = Masiv(5)
print(obj.sub_masiv())