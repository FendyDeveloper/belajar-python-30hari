# PR
# 16 Januari 2024


# try:
#     a = 0
#     nilai = 10 / a
#     print("nilai =", nilai)
# except ZeroDivisionError:
#     print("Nilai tidak boleh 0")
# finally:
#     print("Nilai tidak boleh 0")


def vol_kubus(sisi):
    return sisi ** 3

def vol_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

try:
    print('\nPilih Bangun Ruang : ')
    print('1. Kubus ')
    print('2. Balok ')
    pilihan_bRuang = int(input('Pilihanmu : '))

    if pilihan_bRuang == 1:  # Kubus
        sisi = float(input("Masukkan panjang sisi: "))
        volume = vol_kubus(sisi)
        print(f"Volume Kubus: {volume}")

    elif pilihan_bRuang == 2:  # Balok
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        volume = vol_balok(panjang, lebar, tinggi)
        print(f"Volume Balok: {volume}")

    else:
        print("Pilihan tidak valid untuk bangun ruang.")
except ValueError:
    print('Nilai harus berupa angka 1-8')
