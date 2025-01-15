# FUNCTION
# 12 Januari 2025

def my_information(name, age, address):
    print(f"{name} {age} {address}")

my_information("John", "25", "123 Main Street")

print("==============================================")

def menu(name, price, stock, payment):
    print(f"My name is {name}")
    print(f"{name} price is {price}")
    print(f"stock {name} is {stock}")
    print(f"My payment is {payment}")

menu("John", "25", "123 Main Street", 100)

print("==============================================")

PI = 3.14
def vol_bola(r):
    hasil = (4/3) * PI * (r ** 3)
    print(hasil)

vol_bola(10)

print("==============================================")

def rumus(r):
    volume_bola = (4/3) * PI * (r ** 3)
    luas_lingkaran = PI * (r ** 2)

    return(volume_bola, luas_lingkaran)

volume_bola, luas_lingkaran = rumus(10)
print(volume_bola, luas_lingkaran)

print("==============================================")

#KALKULATOR WITH FUNCTION

def Tampilmenu():
    print('\nPilih Bangun Datar : ')
    print('1. Persegi ')
    print('2. Persegi Panjang ')
    print('3. Segitiga ')
    print('4. Jajar Genjang ')
    print('5. Lingkaran ')
    print('6. Trapesium ')
    print('7. Belah Ketupat ')
    print('8. Layangan ')


def luas_persegi(sisi):
    return sisi * sisi
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
def luas_jajar_genjang(a, t):
    return a * t

def luas_lingkaran(r):
    return 3.14 * (r * r)

def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0.5 * (sisi_atas + sisi_bawah) * tinggi

def luas_layang_layang(diagonal1, diagonal2, diagonal3):
    return diagonal1 * diagonal2 * diagonal3

def vol_kubus(sisi):
    return sisi ** 3

def vol_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

print('Calculator Bangun Datar dan Bangun Ruang!')
print('''Pilih Kategori :
1. Bangun Datar
2. Bangun Ruang ''')
kategori = int(input('Pilihanmu : '))

if (kategori == 1):
    Tampilmenu()
    pilihan_bDatar = int(input('Pilihanmu : '))

    if pilihan_bDatar == 1:  # Persegi
        sisi = float(input("Masukkan panjang sisi: "))
        luas = luas_persegi(sisi)
        print(f"Luas Persegi: {luas}")

    elif pilihan_bDatar == 2:  # Persegi Panjang
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = luas_persegi_panjang(panjang, lebar)
        print(f"Luas Persegi Panjang: {luas}")

    elif pilihan_bDatar == 3:  # Segitiga
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = luas_segitiga(alas, tinggi)
        print(f"Luas Segitiga: {luas}")

    elif pilihan_bDatar == 4:  # Jajar Genjang
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = luas_jajar_genjang(a, t)
        print(f"Luas Jajar Genjang: {luas}")

    elif pilihan_bDatar == 5:  # Lingkaran
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = luas_lingkaran(jari_jari)
        print(f"Luas Lingkaran: {luas}")

    elif pilihan_bDatar == 6:  # Trapesium
        sisi_atas = float(input("Masukkan sisi atas: "))
        sisi_bawah = float(input("Masukkan sisi bawah: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas =  luas_trapesium(sisi_atas, sisi_bawah, tinggi)
        print(f"Luas Trapesium: {luas}")

    elif pilihan_bDatar == 8:  # Layang-Layang
        diagonal_1 = float(input("Masukkan diagonal 1: "))
        diagonal_2 = float(input("Masukkan diagonal 2: "))
        luas = luas_layang_layang(0.5, diagonal_1 * diagonal_2)
        print(f"Luas Layang-Layang: {luas}")

    else:
        print("Pilihan tidak valid.")

elif (kategori == 2):
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

else:
    print("Pilihan kategori tidak valid.")






