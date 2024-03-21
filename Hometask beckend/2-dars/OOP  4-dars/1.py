class Sistema:
    def __init__(self, num):
        self.num = num
    
    def ikki(self):
        return bin(self.num)

    def sakkiz(self):
        return oct(self.num)

    def on_olti(self):
        return hex(self.num)


son = 42

san = Sistema(son)
print(f"10 lik: {son}")
print(f"2 lik: {san.ikki()}")
print(f"8 lik: {san.sakkiz()}")
print(f"16 lik: {san.on_olti()}")
