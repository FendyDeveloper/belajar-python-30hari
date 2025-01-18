import time
import os
import random
from time import sleep
import sys


# Fungsi untuk efek typing
def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Fungsi untuk animasi loading
def loading_animation():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Data karakter yang bisa diselamatkan
characters = {
    "1": {
        "name": "Princess Luna",
        "description": "Putri kerajaan yang terjebak di Menara Kristal",
        "lives": 3,
        "saved": False,
        "difficulty": "Medium",
        "bonus": "Memberi tambahan 1 nyawa untuk karakter selanjutnya",
        "ascii_art": """
        👸
       /|\\
        |
       / \\
        """
    },
    "2": {
        "name": "Wizard Merlin",
        "description": "Penyihir bijak yang terkurung di Gua Kegelapan",
        "lives": 3,
        "saved": False,
        "difficulty": "Hard",
        "bonus": "Bisa skip 1 pertanyaan untuk karakter selanjutnya",
        "ascii_art": """
        🧙‍♂️
       /|\\
        |
       / \\
        """
    },
    "3": {
        "name": "Knight Roland",
        "description": "Ksatria pemberani yang terjebak di Kastil Naga",
        "lives": 3,
        "saved": False,
        "difficulty": "Easy",
        "bonus": "Mendapat 1 kesempatan untuk mengulang jawaban",
        "ascii_art": """
        🤺
       /|\\
        |
       / \\
        """
    }
}

# Bank soal dengan berbagai tingkat kesulitan
questions = {
    "Easy": [
        {
            "question": "Berapakah hasil dari 8 × 9?",
            "options": {"a": "72", "b": "63", "c": "81", "d": "90"},
            "correct": "a",
            "explanation": "8 × 9 = 72"
        },
        {
            "question": "Apa warna langit di siang hari yang cerah?",
            "options": {"a": "Merah", "b": "Biru", "c": "Hijau", "d": "Kuning"},
            "correct": "b",
            "explanation": "Langit berwarna biru di siang hari yang cerah"
        }
    ],
    "Medium": [
        {
            "question": "Berapakah akar kuadrat dari 144?",
            "options": {"a": "10", "b": "11", "c": "12", "d": "13"},
            "correct": "c",
            "explanation": "√144 = 12"
        },
        {
            "question": "Siapa penemu bola lampu?",
            "options": {"a": "Newton", "b": "Edison", "c": "Tesla", "d": "Einstein"},
            "correct": "b",
            "explanation": "Thomas Edison menemukan bola lampu pada tahun 1879"
        }
    ],
    "Hard": [
        {
            "question": "Berapakah hasil dari 15% dari 480?",
            "options": {"a": "62", "b": "72", "c": "82", "d": "92"},
            "correct": "b",
            "explanation": "15% dari 480 = (15/100) × 480 = 72"
        },
        {
            "question": "Dalam sistem tata surya, planet manakah yang memiliki cincin paling terlihat?",
            "options": {"a": "Jupiter", "b": "Uranus", "c": "Saturnus", "d": "Neptunus"},
            "correct": "c",
            "explanation": "Saturnus memiliki cincin yang paling terlihat dari Bumi"
        }
    ]
}


def display_intro():
    clear_screen()
    title = """
    ╔═══════════════════════════════════════════════════════╗
    ║             MISSION: HEROES RESCUE                     ║
    ║          ~ A Quest to Save the Heroes ~               ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(title)
    typewriter("Loading game components...", 0.05)
    loading_animation()

    story = """
    Di sebuah kerajaan yang jauh, tiga pahlawan telah terjebak
    oleh sihir jahat sang Penyihir Kegelapan. Mereka membutuhkan
    bantuan Anda untuk bebas dari kutukan ini.

    Misi Anda adalah menyelamatkan mereka dengan menjawab
    berbagai tantangan dan teka-teki yang akan dihadapi.

    Setiap pahlawan memiliki karakteristik dan bonus unik yang
    dapat membantu dalam penyelamatan pahlawan lainnya.

    Apakah Anda siap untuk memulai petualangan ini?
    """
    typewriter(story, 0.03)
    input("\nTekan ENTER untuk melanjutkan...")


def display_character_selection():
    clear_screen()
    print("\n=== PILIH PAHLAWAN YANG INGIN DISELAMATKAN ===\n")

    for id, char in characters.items():
        if not char["saved"]:
            print(f"\n{id}. {char['name']}")
            print(char['ascii_art'])
            print(f"Status: {'BELUM DISELAMATKAN ❌'}")
            print(f"Kesulitan: {char['difficulty']}")
            print(f"Deskripsi: {char['description']}")
            print(f"Bonus: {char['bonus']}")
            print("-" * 50)

    saved_count = sum(1 for char in characters.values() if char["saved"])
    print(f"\nPahlawan yang telah diselamatkan: {saved_count}/3")

    if saved_count == 3:
        return None

    while True:
        choice = input("\nPilih nomor pahlawan (1-3): ")
        if choice in characters and not characters[choice]["saved"]:
            return choice
        print("Pilihan tidak valid atau pahlawan sudah diselamatkan!")


def play_rescue_mission(character):
    clear_screen()
    char = characters[character]

    print(f"\n=== MISI PENYELAMATAN: {char['name']} ===")
    print(char['ascii_art'])
    print(f"Tingkat Kesulitan: {char['difficulty']}")
    print(f"Nyawa: {'❤️' * char['lives']}")

    # Ambil pertanyaan sesuai tingkat kesulitan
    level_questions = questions[char['difficulty']]
    random.shuffle(level_questions)

    for question in level_questions:
        print("\n" + "=" * 50)
        typewriter(question['question'])

        for option, answer in question['options'].items():
            typewriter(f"{option}) {answer}")

        user_answer = input("\nMasukkan jawaban Anda (a/b/c/d): ").lower()

        if user_answer == question['correct']:
            typewriter("\n✨ BENAR! ✨", 0.05)
            typewriter(question['explanation'])
            char['saved'] = True
        else:
            typewriter("\n❌ SALAH! ❌", 0.05)
            typewriter(question['explanation'])
            char['lives'] -= 1
            print(f"Nyawa tersisa: {'❤️' * char['lives']}")

            if char['lives'] <= 0:
                typewriter(f"\n💔 {char['name']} tidak dapat diselamatkan...")
                return False

        time.sleep(1)

    return char['lives'] > 0


def display_ending():
    clear_screen()
    saved_heroes = [char['name'] for char in characters.values() if char['saved']]

    print("\n=== HASIL AKHIR MISI ===\n")
    typewriter(f"Pahlawan yang berhasil diselamatkan: {len(saved_heroes)}/3")

    for hero in saved_heroes:
        print(f"✅ {hero}")

    if len(saved_heroes) == 3:
        typewriter("\n🎊 SELAMAT! Anda telah menyelesaikan semua misi! 🎊")
    elif len(saved_heroes) > 0:
        typewriter("\n😊 Beberapa pahlawan berhasil diselamatkan!")
    else:
        typewriter("\n😢 Sayang sekali, tidak ada pahlawan yang berhasil diselamatkan...")


def main():
    display_intro()

    while True:
        character_choice = display_character_selection()
        if character_choice is None:
            display_ending()
            break

        if play_rescue_mission(character_choice):
            typewriter(f"\n🎉 {characters[character_choice]['name']} berhasil diselamatkan!\n")
        else:
            typewriter(f"\n💔 {characters[character_choice]['name']} tidak dapat diselamatkan...\n")

        time.sleep(2)
        clear_screen()


if __name__ == "__main__":
    main()