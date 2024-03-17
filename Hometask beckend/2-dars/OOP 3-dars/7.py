class Bank:
    def __init__(self, pul, foiz):
        self.pul = pul  
        self.foiz = foiz  

    def foyda(self):
        foyda = 0
        for i in range(len(self.pul)):
            foyda += self.pul[i] * self.foiz[i] / 100  
        return foyda

pul = [1000, 2000, 3000]  
foiz = [5, 7, 10]  
 
bank = Bank(pul, foiz)

foyda = bank.foyda()

print("Bank bir yilda", foyda, "foyda ko'radi.")
