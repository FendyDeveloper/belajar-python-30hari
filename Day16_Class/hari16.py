# CLASS
# 18 Januari 2025

# class Mobil:
#     def __init__(self, x, y, w, h):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#
#     def draw(self):
#         if self.h == False:
#             print("True")
#         else:
#             print("False")


# mobil = Mobil('Mobil', 'Mobil', 'Mobil', False)
# mobil.draw()

class Mahasiswa:
    def __init__(self, nama, fakultas, ipk, universitas):
        self.nama = nama
        self.fakultas = fakultas
        self.ipk = ipk
        self.universitas = universitas

    def show_name(self):
        print(f'Nama : {self.nama}')

    def show_fakultas(self):
        print(f'Fakultas : {self.fakultas}')

    def show_ipk(self):
        print(f'IPK : {self.ipk}')

    def show_universitas(self):
        print(f'Universitas : {self.universitas}')

check_data_status = True
while check_data_status:
    print("========= INPUT DATA MAHASISWA ==========")
    nama = input("Masukkan nama : ")
    fakultas = input("Masukkan fakultas : ")
    ipk = float(input("Masukkan ipk : "))
    universitas = input("Masukkan universitas : ")
    print("========= OUTPUT DATA MAHASISWA ==========")
    print(f"Nama anda : {nama}")
    print(f"Fakultas : {fakultas}")
    print(f"Ipk : {ipk}")
    print(f"Universitas : {universitas}")
    check_data = input("Apakah data anda sudah benar? (y/n) : ")
    if check_data == "y":
        print("========= DATA MAHASISWA ==========")
        save_data = Mahasiswa(nama, fakultas, ipk, universitas)
        save_data.show_name()
        save_data.show_fakultas()
        save_data.show_ipk()
        save_data.show_universitas()
        check_data_status = False
    elif check_data == "n":
        check_data_status = True
    else:
        print("input y/n bro")

