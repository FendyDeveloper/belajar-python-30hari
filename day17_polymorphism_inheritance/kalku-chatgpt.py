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
        if angka2 == 0:
            return "Error: Pembagian dengan nol tidak diperbolehkan."
        return angka1 / angka2


class Scientific(Main):
    def __init__(self):
        super().__init__()

    def penjumlahan_sin(self, radian1, radian2):
        hasil = self.penjumlahan(math.sin(radian1), math.sin(radian2))
        print(f"sin({radian1}) = {math.sin(radian1):.4f}")
        print(f"sin({radian2}) = {math.sin(radian2):.4f}")
        print(f"Hasil penjumlahan sin: {hasil:.4f}")
        print("=" * 30)

    def pengurangan_cos(self, radian1, radian2):
        hasil = self.pengurangan(math.cos(radian1), math.cos(radian2))
        print(f"cos({radian1}) = {math.cos(radian1):.4f}")
        print(f"cos({radian2}) = {math.cos(radian2):.4f}")
        print(f"Hasil pengurangan cos: {hasil:.4f}")
        print("=" * 30)

    def perkalian_tan(self, radian1, radian2):
        hasil = self.perkalian(math.tan(radian1), math.tan(radian2))
        print(f"tan({radian1}) = {math.tan(radian1):.4f}")
        print(f"tan({radian2}) = {math.tan(radian2):.4f}")
        print(f"Hasil perkalian tan: {hasil:.4f}")
        print("=" * 30)

    def pembagian_sin(self, radian1, radian2):
        sin1 = math.sin(radian1)
        sin2 = math.sin(radian2)
        hasil = self.pembagian(sin1, sin2)
        print(f"sin({radian1}) = {sin1:.4f}")
        print(f"sin({radian2}) = {sin2:.4f}")
        if isinstance(hasil, str):  # Cek jika hasil adalah pesan error
            print(hasil)
        else:
            print(f"Hasil pembagian sin: {hasil:.4f}")
        print("=" * 30)


# Main program
print("========== KALKULATOR ==========")
try:
    angka1 = float(input("Masukkan angka 1 (radian): "))
    angka2 = float(input("Masukkan angka 2 (radian): "))

    print("\n============ HASIL =============")
    sci = Scientific()
    sci.penjumlahan_sin(angka1, angka2)
    sci.pengurangan_cos(angka1, angka2)
    sci.perkalian_tan(angka1, angka2)
    sci.pembagian_sin(angka1, angka2)

except ValueError:
    print("Error: Harap masukkan angka yang valid.")
