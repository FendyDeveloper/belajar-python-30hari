#KELAS TANOK HARI 3
#05 Januari 2025

#LIST Nama nama teman terdekat

names = ['Nanda', 'Raihan', 'Wildan', 'Anggun']

friend = names[0]
print(f"My best friend : {friend}")

names.append('Frisilia')
print(names)
names.remove(friend)
print(names)
names.pop()
print(names)
names.insert(0, 'Ayush')
print(names)

#Clear List
angka = [1,2,3,4,5,9,6,8,9]
# angka.clear()
angka.sort(reverse=True)
print(angka * 4)