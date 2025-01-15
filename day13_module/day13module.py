# 15 Januari 2025
# Import Library

# import math
#
# hasil = math.sin(math.radians(45))
#
# print(f"{hasil:.2f}")

# from math import sqrt
#
# hasil = sqrt(6)
# print(hasil)

# import random
#
# print(random.random())
# print(random.randint(1, 3))
#
# list_name = ['Fendy', 'Nala', 'Bags']
# print(random.choice(list_name))
# print(random.choices(list_name, k=7))
# print(random.sample(list_name, k=7))

# import my_module as m
# m.sapa_kamu('Fendty')

# password = rnd.choices(all_chars, k=len(all_chars))
# print(password)
# for char in password:
#     rnd.choices(char, k=4)

# for _ in range(panjang_password):
#     password += rnd.choice(all_chars)
#
# print("Password Anda:", password)

import random as rnd

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
simbol = "{}[])(*&^%$#@!?"

all_chars = lower + upper + numbers + simbol


password = ""
panjang_password = int(input("Masukkan panjang password: "))
for char in range(8):
    password += rnd.choice(all_chars)

print(password)

