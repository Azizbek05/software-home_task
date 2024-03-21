class YON_DAFTAR:
    def __init__(self):
        self.daftar = {}

    def yozuv_qoshish(self, ism, malumot):
        self.daftar[ism] = malumot
        print(f"{ism} yozuvi muvaffaqiyatli qo‘shildi.")

    def yozuv_ochirish(self, ism):
        if ism in self.daftar:
            del self.daftar[ism]
            print(f"{ism} yozuvi muvaffaqiyatli o‘chirildi.")
        else:
            print(f"{ism} nomi bilan yozuv topilmadi.")

    def yozuvni_izlash(self, sorovnoma):
        if sorovnoma in self.daftar:
            print(f"{sorovnoma}: {self.daftar[sorovnoma]}")
        else:
            print(f"{sorovnoma} nomi bilan yozuv topilmadi.")

    def barcha_yozuvlarni_korsatish(self):
        print("YON_DAFTAR daftari:")
        for ism, malumot in self.daftar.items():
            print(f"{ism}: {malumot}")
