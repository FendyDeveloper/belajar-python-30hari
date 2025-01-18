#16 Januari 2025
#Game Selamatkan Budi

#GAME 1
# nyawa = 5
# jawab = input("Masukan jawaban : ")
# key = 'alam'
#
# if key == jawab:
#     print("Selamat jawaban anda benar")
# else:
#     print("Woy jawaban anda salah")
#     nyawa -= 1
#     print(f"Jumlah nyawa {nyawa}")
#
# if nyawa == 5:
#     print(f"Nyawa sisa : {nyawa}")
# elif nyawa == 4:
#     print(f"Nyawa sisa : {nyawa}")
# elif nyawa == 3:
#     print(f"Nyawa sisa : {nyawa}")
# elif nyawa == 2:
#     print(f"Nyawa sisa : {nyawa}")
# elif nyawa == 1:
#     print(f"Nyawa sisa : {nyawa}")
# else:
#     print(f"Budi Mati")

#GAME 2
# # Inisialisasi jumlah nyawa
# nyawa = 5
# # Kunci jawaban yang benar
# key = 'alam'
#
# # Loop sampai nyawa habis atau jawaban benar
# while nyawa > 0:
#     jawab = input("Masukan jawaban: ")
#
#     # Cek apakah jawaban benar
#     if key == jawab:
#         print("Selamat jawaban anda benar")
#         break
#     else:
#         nyawa -= 1
#         print(f"Woy jawaban anda salah. Jumlah nyawa sisa: {nyawa}")
#
# # Jika nyawa habis dan jawaban masih salah
# if nyawa == 0:
#     print("Game over! Budi Mati")

# List of dictionaries untuk menyimpan soal dan jawaban
# soal_jawaban = [
#     {
#         'soal': "Apa ibu kota Indonesia?",
#         'a': "Jakarta",
#         'b': "Bandung",
#         'c': "Surabaya",
#         'd': "Bali",
#         'jawaban': 'a'
#     },
#     {
#         'soal': "Apa nama ibu kota Jepang?",
#         'a': "Osaka",
#         'b': "Tokyo",
#         'c': "Kyoto",
#         'd': "Nagoya",
#         'jawaban': 'b'
#     },
#     {
#         'soal': "Apa nama ibu kota Prancis?",
#         'a': "Marseille",
#         'b': "Lyon",
#         'c': "Paris",
#         'd': "Nice",
#         'jawaban': 'c'
#     }
# ]
#
# # Contoh penggunaan: Menampilkan soal dan memeriksa jawaban
# for item in soal_jawaban:
#     print(item['soal'])
#     print(f"a. {item['a']}")
#     print(f"b. {item['b']}")
#     print(f"c. {item['c']}")
#     print(f"d. {item['d']}")
#
#     jawab = input("Masukkan jawaban (a/b/c/d): ")
#
#     if jawab == item['jawaban']:
#         print("Selamat, jawaban anda benar!\n")
#     else:
#         print("Maaf, jawaban anda salah.\n")

import time
import os
import random
from time import sleep
import sys


# Fungsi untuk animasi loading
def loading_animation():
    animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\r" + "Loading " + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Fungsi untuk animasi teks
def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# Fungsi untuk banner game
def print_banner():
    banner = """
    ╔═══════════════════════════════════════════════════╗
    ║             🎮 MISSION: SAVE THEM ALL 🎮          ║
    ║          A Hero's Journey to Save Lives!          ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(banner)


# Data karakter yang bisa diselamatkan
characters = [
    {
        "id": 1,
        "name": "Princess Luna",
        "description": "Putri kerajaan yang terjebak di menara tertinggi",
        "lives": 3,
        "saved": False,
        "difficulty": "Medium",
        "symbol": "👸"
    },
    {
        "id": 2,
        "name": "Sir Knight",
        "description": "Ksatria kerajaan yang terjebak di gua naga",
        "lives": 3,
        "saved": False,
        "difficulty": "Hard",
        "symbol": "⚔️"
    },
    {
        "id": 3,
        "name": "Wizard Merlin",
        "description": "Penyihir bijak yang terkurung oleh sihir jahat",
        "lives": 3,
        "saved": False,
        "difficulty": "Easy",
        "symbol": "🧙‍♂️"
    },
    {
        "id": 4,
        "name": "Little Tommy",
        "description": "Anak kecil yang tersesat di hutan gelap",
        "lives": 3,
        "saved": False,
        "difficulty": "Easy",
        "symbol": "👦"
    },
    {
        "id": 5,
        "name": "Queen Aurora",
        "description": "Ratu yang dikutuk dalam tidur abadi",
        "lives": 3,
        "saved": False,
        "difficulty": "Hard",
        "symbol": "👑"
    }
]

# Bank soal dengan tingkat kesulitan
questions = [
    {
        "difficulty": "Easy",
        "question": "Berapakah hasil dari 8 × 4?",
        "options": {"a": "24", "b": "32", "c": "28", "d": "36"},
        "correct": "b",
        "explanation": "8 × 4 = 32"
    },
    {
        "difficulty": "Medium",
        "question": "Jika 3x + 5 = 20, berapakah nilai x?",
        "options": {"a": "5", "b": "7", "c": "3", "d": "8"},
        "correct": "a",
        "explanation": "3x + 5 = 20 → 3x = 15 → x = 5"
    },
    {
        "difficulty": "Hard",
        "question": "Akar kuadrat dari 144 adalah...",
        "options": {"a": "10", "b": "12", "c": "14", "d": "16"},
        "correct": "b",
        "explanation": "√144 = 12"
    },
    # Tambahkan lebih banyak soal sesuai kebutuhan
]


def show_character_status(character):
    print(f"\n{character['symbol']} {character['name']}")
    print(f"{'▰' * character['lives']}{'▱' * (3 - character['lives'])} ({character['lives']} nyawa)")
    print(f"Status: {'✅ Selamat' if character['saved'] else '❌ Belum Selamat'}")
    print(f"Tingkat Kesulitan: {character['difficulty']}")
    print(f"Deskripsi: {character['description']}")


def choose_character():
    clear_screen()
    print_banner()
    print_slow("\n=== PILIH KARAKTER YANG INGIN DISELAMATKAN ===\n")

    available_characters = [char for char in characters if not char['saved']]

    if not available_characters:
        print_slow("🎉 SELAMAT! Semua karakter telah diselamatkan! 🎉")
        return None

    print("Karakter yang tersedia untuk diselamatkan:")
    for char in available_characters:
        print(f"\n{char['id']}. {char['symbol']} {char['name']}")
        print(f"   └─ {char['description']}")
        print(f"   └─ Tingkat Kesulitan: {char['difficulty']}")

    while True:
        try:
            choice = int(input("\nPilih nomor karakter (1-5): "))
            selected_character = next((char for char in available_characters if char['id'] == choice), None)
            if selected_character:
                return selected_character
            print("❌ Pilihan tidak valid atau karakter sudah diselamatkan!")
        except ValueError:
            print("❌ Masukkan nomor yang valid!")


def play_rescue_mission(character):
    clear_screen()
    print_banner()
    print_slow(f"\n🎯 MISI: Menyelamatkan {character['symbol']} {character['name']}!")
    print_slow(f"📜 {character['description']}")

    # Pilih soal sesuai tingkat kesulitan
    available_questions = [q for q in questions if q['difficulty'] == character['difficulty']]
    question = random.choice(available_questions)

    while character['lives'] > 0 and not character['saved']:
        print("\n" + "=" * 50)
        show_character_status(character)
        print("\n📝 PERTANYAAN:")
        print_slow(question['question'])

        # Tampilkan opsi
        for option, answer in question['options'].items():
            print_slow(f"{option}) {answer}")

        # Animasi thinking
        print("\nBerpikir", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n")

        answer = input("Masukkan jawaban (a/b/c/d): ").lower()

        if answer == question['correct']:
            print_slow("\n✨ SELAMAT! Jawaban Anda benar! ✨")
            print_slow(f"📝 Penjelasan: {question['explanation']}")
            character['saved'] = True
            print_slow(f"\n🎉 {character['name']} berhasil diselamatkan! 🎉")
        else:
            character['lives'] -= 1
            if character['lives'] > 0:
                print_slow(f"\n❌ Jawaban salah! Nyawa tersisa: {character['lives']}")
            else:
                print_slow(f"\n💔 {character['name']} tidak dapat diselamatkan...")

        time.sleep(2)


def main_game():
    clear_screen()
    print_banner()
    loading_animation()

    print_slow("\n=== SELAMAT DATANG DI MISSION: SAVE THEM ALL! ===")
    print_slow("Dalam game ini, Anda akan menjadi seorang pahlawan yang bertugas")
    print_slow("menyelamatkan para karakter yang terjebak dalam berbagai situasi.")
    print_slow("Setiap karakter memiliki 3 nyawa dan tingkat kesulitan berbeda.")
    print_slow("Jawablah pertanyaan dengan benar untuk menyelamatkan mereka!")

    input("\nTekan ENTER untuk memulai petualangan...")

    while True:
        selected_character = choose_character()
        if not selected_character:
            break

        play_rescue_mission(selected_character)

        saved_count = sum(1 for char in characters if char['saved'])
        print(f"\nKarakter yang telah diselamatkan: {saved_count}/5")

        if saved_count < 5:
            continue_game = input("\nIngin menyelamatkan karakter lain? (y/n): ").lower()
            if continue_game != 'y':
                break

    # Tampilkan hasil akhir
    clear_screen()
    print_banner()
    print_slow("\n=== HASIL AKHIR MISI ===")

    saved_count = sum(1 for char in characters if char['saved'])
    print(f"\nKarakter yang berhasil diselamatkan: {saved_count}/5")

    for char in characters:
        status = "SELAMAT ✅" if char['saved'] else "TIDAK SELAMAT ❌"
        print(f"\n{char['symbol']} {char['name']}: {status}")

    if saved_count == 5:
        print_slow("\n🎊 SELAMAT! Anda telah menyelamatkan semua karakter! 🎊")
    elif saved_count > 0:
        print_slow(f"\n👏 Anda berhasil menyelamatkan {saved_count} karakter!")
    else:
        print_slow("\n😢 Sayang sekali, tidak ada karakter yang selamat!")

if __name__ == "__main__":
    main_game()

