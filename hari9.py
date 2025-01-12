# Nested Loop
# 11 Januari 2025
# from hari4 import data_mahasiswa

# print("==========================================")
# for i in range(1,11):
#     for j in range(1,11):
#         hasil = i * j
#         print(f"Hasil dari {i} x {j} : {hasil}")
print("=========================================")

#Matrik List

A = [[4,3, 4],
     [5,6, 4],
     [7,8, 4]]

B = [[1,2, 4],
     [3,4, 4],
     [5,6,4]]

C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# for i in range(0,len(A)):
#     print("[", end=" ")
#     for j in range(0,len(A[0])):
#         C[i][j] = A[i][j] + B[i][j]
#         # print(A[i][j],end=' ')
#         # print(B[i][j],end=' ')
#         # print(C[i][j],end=' ')
#         print(A[i][j] - B[i][j], end=" ")
#     print("]")
print(len(A[0]))
for i in range(0,len(A)):
    for j in range(0,len(B[0])):

        # print(j)
        # print("[", end=" ")
        for k in range(0,len(B)):
            C[i][j] += A[i][k] * B[k][j]
            # print(C[i][j], end=" ")
            # print(f" I : {i}")
            # print(f" J : {j}")
            # print(f"{C[i][j]}", end=" ")
    #     print("]", end=" ")
    # print(" ")
print("Matriks A : ")
for matriksA in A:
    print(matriksA)

print("Matriks B : ")
for matriksB in B:
    print(matriksB)

print("Matriks C = A * B : ")
for matriksC in C:
    print(matriksC)

print("==========================================")

print("Proses Perhitungan:")
for i in range(0,len(A)):
    for j in range(0,len(B[0])):
        C[i][j] = 0  # Reset nilai sebelum perhitungan
        for k in range(0,len(B)):
            # Perkalian matriks yang benar: A[i][k] * B[k][j]
            C[i][j] += A[i][k] * B[k][j]
            print(f" A[{i}][{k}] × B[{k}][{j}] = {A[i][k]} × {B[k][j]} = {A[i][k] * B[k][j]}")
        print(f" Hasil C[{i}][{j}] = {C[i][j]}")
    print(" ")

print("\nHasil Matriks C:")
for row in C:
    print(row)

print("===========================================")

kamus = {'nama' : 'Fendy',
         'age' : 13}
for key, value in kamus.items():
    print(f"{key} : {value}")

print("===========================================")

data_mahasiswa = ['ajen', 'nanda', 'firsa']
for idx, value in enumerate(data_mahasiswa):
    print(f"{idx} : {value}")








































# def
# def greeting(name):
#     """Function to display a greeting"""
#     return f"Hello, %s!!!" % name
#
# print(greeting("Bob"))
#
# def introduction(name, age, job="student"):
#     """Function to display introduction"""
#     return f"My name is {name}, I'm {age} years old, and I work as a {job}!"
#
# print(introduction("Fendy", 21, "Police"))
#
# def process_scores(*args, **kwargs):
#     print("Scores : ", args)
#     print("Other info: ", kwargs)
#
# process_scores(90, 18,12, name="Fendy", cls="12A")

#LOOPING
