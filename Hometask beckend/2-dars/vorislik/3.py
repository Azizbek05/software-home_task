class Kitob:
    def __init__(self, nomi, muallif, yil, nashriyoti):
        self.nomi = nomi
        self.muallif = muallif
        self.yil = yil
        self.nashriyoti = nashriyoti

    def malumot(self):
        print("Kitoblar")
        print(f"Kitob nomi {self.nomi}")
        print(f"Kitob muallif {self.muallif}")
        print(f"Kitob yil {self.yil}")
        print(f"Kitob nashriyoti {self.nashriyoti}")

class UY_KUTUBXONASI(Kitob):
    def __init__(self, uy_manzili,familiya, ism):
        self.uy_manzili = uy_manzili
        self.familiya = familiya
        self.ism = ism
        super().__init__(uy_manzili, familiya, ism)

    def malumot(self):
        print("Malumotlar")
        print(f"uy_manzili {self.uy_manzili}")
        print(f"familiya {self.familiya}")
        print(f"ism {self.ism}")
        super().malumot()


        
kitob = Kitob("garri","Alexsandr",2000, 'bilim.uz')
print(kitob.malumot())


kitobb = UY_KUTUBXONASI("toshkent","Amindjanov","Aziz")
print(kitobb.malumot())