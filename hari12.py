# File Handling
# 14 Januari 2025

# file = open(r'files/hari12.txt', 'w') #Write
# file.write("Hello World")
# file.close()
#
# read = open('files/hari12.txt', 'r') #Read
# print(read.read())
# read.close()
#
# append = open('files/hari12.txt', 'a') #Append
# name = "FendyDev"
# append.write(name)
# append.close()
#
# surat_from = "Fendy"
# surat_to = "Kamu"
#
# surat_text = "01100001 01101011 01110101 01100011 01101001 01101110 01110100 01100001 01110000 01100001 01100100 01100001 01101101 01110101"
# surat = open('files/akupadamu.txt', 'w')
#
# surat.write(f"{surat_from}"
#             f"{surat_to}"
#             f"{surat_text}"
#             f"{surat_from}")
# surat.close()

print("===========================")
print("GAME TEBAK ANGKA")

with open(r'files\history_game.txt', 'r+') as read:
    file_content = read.readlines()
    print("======= History Win =======")
    print(f"Username: {file_content[0]}")
    print(f"Jumlah Percobaan: {file_content[1]}")
    print("===========================")

    username = input("Enter Username: ")
    percobaan = 0
    final = 10
    while True:
        number = int(input("Enter numbers: "))
        percobaan += 1
        if number < final:
            print("Angka Terlalu Kecil")
        elif number > final:
            print("Angka Terlalu Besar")
        else:
            print(f"Selamat {username} Tebakan anda benar")
            break
    with open(r'files\history_game.txt', 'w') as file:

        file.write(f"{username}\n" )
        file.write(f"{percobaan}" )

print("====================================")