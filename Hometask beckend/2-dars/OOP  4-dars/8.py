class TALABA_GURUHI:
    def __init__(self):
        self.guruh = {}

    def qoshish(self, ism, malumot):
        self.guruh[ism] = malumot
        print(f"{ism} talabasi guruhga muvaffaqiyatli qo‘shildi.")

    def ochirish(self, ism):
        if ism in self.guruh:
            del self.guruh[ism]
            print(f"{ism} talabasi guruhdan muvaffaqiyatli ochirildi.")
        else:
            print(f"{ism} nomli talaba guruhda topilmadi.")

    def izlash(self, sorovnoma):
        if sorovnoma in self.guruh:
            print(f"{sorovnoma}: {self.guruh[sorovnoma]}")
        else:
            print(f"{sorovnoma} nomli talaba guruhda topilmadi.")

    def guruhni_tartiblash(self):
        sorted_guruh = sorted(self.guruh.items(), key=lambda x: x[0])
        self.guruh = dict(sorted_guruh)
        print("Guruh tartiblangan.")

    def guruhni_korsatish(self):
        print("Guruhda mavjud talabalar:")
        for ism, malumot in self.guruh.items():
            print(f"{ism}: {malumot}")
