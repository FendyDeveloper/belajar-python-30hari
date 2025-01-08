#Conditional
#08 Januari 2024

#if else
data = "lapar"
point = 21

if data == "lapar":
    print("Aku Lapar")

if (point <= 100) and (point > 79):
    print("Your point is A", point)

elif (point <= 79) and (point > 50):
    print("Your point is B", point)

elif (point <= 50) and (point >= 0):
    print("Your point is C", point)

else:
    print("Input Number 0-100 bukan", point)

print("=======================================")

bangun_tidur = True
mandi = True
berangkat_sekolah = True
dihukum_sekolah = True
if bangun_tidur:
    print("Bangun")
    if mandi:
        print("Tumben Mandi")
        if berangkat_sekolah:
            print("Tumben Berangkat Sekolah")
            if dihukum_sekolah:
                print("Mampuss Dihukum Sekolah")
            else:
                print("Tumben Sekolah")
        else:
            print("hadeh malah ga Sekolah")
    else:
        print("Buruan Mandi Woy")
else:
    print("Bangun bangun woy")

print("=======================================")

#Membuat sebuah program, yang menyimpan daftar nama

list_nama = ['Asep', 'Juned', 'Alamiah']
list_baju = ['Merah', 'Biru', 'Kuning']
input_nama = input("Input nama: ")
input_baju = input("Input baju: ")


for nama in list_nama:
    if nama == input_nama:
        for baju in list_baju:
            if input_baju == baju:
                print(f"Cowok {baju}flag")
            else:
                print(f"{nama} Cowok {baju}flag")
            break
    else:
        print("Cowok GreenFlag")
    break

print("=======================================")




