# FOR LOOPING
# 10 Januari 2024

# angka = [1,2,3,4,5,6,7,8,9,3,4,5,6,4,6,6,4,4,8,6,7,6,7,7,7]
# print(len(angka))
# for i in range(len(angka)):
#     print(angka[i])

#Bilangan faktorial

# nilai = int(input("Masukkan nilai: "))
# hasil = 1
# for i in range(nilai, 0, -1):
#     hasil *= i

# print(hasil)

# Looping di dalam Looping (nested)
# for i in range(1, 11):
#     for j in range(1, 11):
        # print(f"Nilai {i}, Nilai {j}")

for i in range(1,11):
    # print(1 * i)
    print(i * i)
    # print(i)

print("==========================================")
for i in range(1,11):
    for j in range(1,11):
        hasil = i * j
        print(f"Hasil dari {i} x {j} : {hasil}")
    print("=========================================")
