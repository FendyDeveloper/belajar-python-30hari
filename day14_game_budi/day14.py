#16 Januari 2025
#Game Selamatkan Budi

nyawa = 5
jawab = input("Masukan jawaban : ")
key = 'alam'

if key == jawab:
    print("Selamat jawaban anda benar")
else:
    print("Woy jawaban anda salah")
    nyawa -= 1
    print(f"Jumlah nyawa {nyawa}")

if nyawa == 5:
    print(f"Nyawa sisa : {nyawa}")
elif nyawa == 4:
    print(f"Nyawa sisa : {nyawa}")
elif nyawa == 3:
    print(f"Nyawa sisa : {nyawa}")
elif nyawa == 2:
    print(f"Nyawa sisa : {nyawa}")
elif nyawa == 1:
    print(f"Nyawa sisa : {nyawa}")
else:
    print(f"Budi Mati")

# while True:
#     nyawa -= 1
#     if sisa_nyawa == nyawa:
#         print(f"Nyawa sisa : {sisa_nyawa}")