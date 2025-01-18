#GAME
import random
import bahan
is_ready = True
nyawa = 5
print(bahan.title)
if is_ready:
    pertanyaan_file = open('pertanyaan.txt', 'r')
    jawaban_file = open('jawaban.txt', 'r')
    pertanyaan_list = pertanyaan_file.readlines()
    jawaban_list = jawaban_file.readlines()
    for sisa_nyawa in range(0, 5):
        # print(jawaban[sisa_nyawa])
        angka_random = random.randint(0, len(pertanyaan_list) - 1)
        pertanyaan = pertanyaan_list[angka_random].strip()
        jawaban = jawaban_list[angka_random].strip()

        print(f"Pertanyaan: {pertanyaan}")

        user_answer = input("Jawaban : ")
        if user_answer.lower() == jawaban.lower():
            # is_ready = False
            print("Selamat anda berhasil")
            break
        else:
            nyawa -= 1
            print(f"Jawaban salah! Sisa nyawa Anda: {nyawa}")

        if nyawa == 0:
            print("Nyawa telah habis")

    pertanyaan.close()
    jawaban.close()

print(f'Terima kasih')





