#04 Januari 2025

import math
#Luas lingkaran
pi = 22 / 7
r = 7

hasil = math.pi * (r ** 2)
print(math.pi)

print(hasil)

#Operator perbandingan
# a = int(input("Masukan angka : "))
# b = int(input("Masukan angka : "))

a = 1
b = 2

print("Operator Perbandingan")
print(f"apakah nilai {a} == {b}?: {a == b}")
print(f"{a != b}")
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

#Operator logika

print("OPERATOR LOGIKA")
print((a > b) & (a < b))
print((a > b) and (a < b))
kopi = "ayam"
pitik = "ikan"
print(kopi == "ayam" and pitik == "ikan")

#Harga Final Sepatu

sepatu = 120000
diskon = 10 / 100
PPN = 12 / 100

hasil = (sepatu - (diskon * sepatu) - (PPN * sepatu))
print(f"Harga Sepatu: {sepatu}")
print(f"Harga Diskon 10%: {diskon * sepatu}")
print(f"PPN 12%: {PPN * sepatu}")
print(f"Total bayar : {hasil}")

