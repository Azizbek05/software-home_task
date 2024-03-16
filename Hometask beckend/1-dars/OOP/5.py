class Ifodalash:
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def son(self):
        sonlar = {
            0:'nol',
            1:"bir",
            2:"ikki",
            3:"uch",
            4:"tort",
            5:"besh",
            6:'olti',
            7:"yetti",
            8:"sakiz",
            9:"toqiz"
        }
         
        return sonlar.get(self.a)
    
    def hafta(self):
        hafta = {
            1:"Dushanba",
            2:"Seshanba",
            3:"Chorshanba",
            4:"Payshanba",
            5:"Juma",
            6:"Shanba",
            7:"Yakshanba",
        }

        return hafta.get(self.b)
    

    def oy(self):
        oy = {
            1:"Yanvar",
            2:"Fevral",
            3:"Mart",
            4:"Aprel",
            5:"May",
            6:"Iyun",
            7:"Iyul",
            8:"Avgust",
            9:"Sentyabr",
            10:"Oktyabr",
            11:"Noyabr",
            12:"Dekabr"
        }

        return oy.get(self.c)
    

a = int(input("0 dan 9 gacham son kiriting: "))
b = int(input("0 dan 7 gacham son kiriting: "))
c= int(input("0 dan 12 gacham son kiriting: "))

obj = Ifodalash(a,b,c)

print(f"Raqam = {obj.son()}")

print(f"Hafta = {obj.hafta()}")

print(f"Oy = {obj.oy()}")