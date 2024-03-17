class DoiraSanash:
    def __init__(self, a):
        self.a = a

    def sanash(self, k):
        n = len(self.a) 
        count = 0  

        for i in range(n):
            if self.a[i] == k:
                count += 1

        return count

a = [1, 3, 2, 3, 4, 3, 5, 6, 3]  

k = int(input("son kiriting: "))

doira = DoiraSanash(a)

nechta = doira.sanash(k)

print(f"Doirada {k} soniga teng bo'lgan elementlar soni: {nechta}")
