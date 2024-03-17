class Supermarket:
    def __init__(self,soni, narxi, sotilgan):
        self.soni = soni
        self.narxi = narxi
        self.sotilgan = sotilgan

    def tekshir(self):
        summa = [self.narxi[i] * self.sotilgan[i] for i in range(len(self.soni)) ]
        

        qolgan_narsa = [] 
        for i in range(len(self.soni)):
            qolgan_narsa.append(self.soni[i] - self.sotilgan[i])

        return f"Jami hisobda {summa} hisobida narsa sotilgan {qolgan_narsa} qoldi"
    

soni = [5, 10, 8]
narxi = [20, 50, 12]
sotilgan = [2, 4 , 3]


obj = Supermarket(soni, narxi, sotilgan)

print(obj.tekshir())