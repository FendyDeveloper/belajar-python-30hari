# Input and Output
# 07 Januari 2024

#Input
name = input("What is your name?: ").lower()
print(f"Hello, {name}")
print(type(name))
print(bool(name))

age = int(input("Input your age: "))
print(f"You are {age} years old")
print(type(age))

address = input("Input your address (true/false): ").lower()
address = address == "true"
print(address)
print(type(address))

#OUTPUT
name = "Namaku adalah Junaidiasepjayamurnisepantas"
age = 12
bb = 7777.72
print(f"Hello, {name}")
print(f"Your age is {age} years old")
print(f"BB mu is {bb * 1999} kg")

pi = 22/7
print(f"{pi} pi is {pi:.3f}")

print("=========PROGRAM HITUNG VOLUME TABUNG=========")
r = float(input("Masukan jari-jari tabung : "))
t = float(input("Masukan tinggi tabung : "))
pi = 22/7

v = pi * (r**2) * t

print("=========HASIL PROGRAM HITUNG VOLUME TABUNG=========")
print(f"Jari-jari tabung: {r}")
print(f"Tinggi tabung: {t}")
print(f"pi = {pi:.2f}")
print(f"\nRumus Menghitung Volume Tabung\nV = pi * (r**2) * t")

print(f"Jadi Volume Tabung : {v}")
print("====================================================")

