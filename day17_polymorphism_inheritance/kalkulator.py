import math

class Main:
    def __init__(self):
        pass

    def penjumlahan(self, angka1, angka2):
        return angka1 + angka2
    def pengurangan(self, angka1, angka2):
        return angka1 - angka2
    def perkalian(self, angka1, angka2):
        return angka1 * angka2
    def pembagian(self, angka1, angka2):
        return angka1 / angka2

class Scientific(Main):
    def __init__(self):
        super().__init__()

    def penjumlahan_sin(self, radian1, radian2):
        self.radian1 = radian1
        self.radian2 = radian2
        self.hasil = self.penjumlahan(math.sin(radian1), math.sin(radian2))
        print(f"Hasil dari sin {self.radian1} = {math.sin(self.radian1)}")
        print(f"Hasil dari sin {self.radian2} = {math.sin(self.radian2)}")
        print(f"Hasil sin {math.sin(self.radian1)} + sin {math.sin(self.radian2)} : {self.hasil}")
        print("=============================")

    def pengurangan_cos(self, radian1, radian2):
        self.radian1 = radian1
        self.radian2 = radian2
        self.hasil = self.pengurangan(math.cos(radian1), math.cos(radian2))
        print(f"Cos dari {self.radian1} = {math.cos(radian1)}")
        print(f"Cos dari {self.radian2} = {math.cos(radian2)}")
        print(f"Hasil {math.cos(self.radian1)} - {math.cos(self.radian2)} : {self.hasil}")
        print("=============================")

    def perkalian_tan(self, radian1, radian2):
        self.radian1 = radian1
        self.radian2 = radian2
        self.hasil = self.perkalian(math.sin(radian1), math.sin(radian2))
        print(f"Hasil dari tan {self.radian1} = {math.tan(self.radian1)}")
        print(f"Hasil dari tan {self.radian2} = {math.tan(self.radian2)}")
        print(f"Hasil tan {math.tan(self.radian1)} * tan {math.tan(self.radian2)} : {self.hasil}")
        print("=============================")

    def pembagian_sin(self, radian1, radian2):
        self.radian1 = radian1
        self.radian2 = radian2
        self.hasil = self.pembagian(math.sin(radian1), math.sin(radian2))
        print(f"Hasil dari sin {self.radian1} = {math.sin(self.radian1)}")
        print(f"Hasil dari sin {self.radian2} = {math.sin(self.radian2)}")
        print(f"Hasil pembagian sin {math.sin(self.radian1)} / sin {math.sin(self.radian2)} : {self.hasil}")
        print("=============================")

print("========== KALKULATOR ==========")
angka1 = float(input("angka 1: "))
angka2 = float(input("angka 2: "))
sci = Scientific()
print("============ HASIL =============")
sci.penjumlahan_sin(angka1, angka2)
sci.pengurangan_cos(angka1, angka2)
sci.perkalian_tan(angka1, angka2)
sci.pembagian_sin(angka1, angka2)

