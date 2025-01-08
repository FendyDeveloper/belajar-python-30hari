#Tuple dan Dictionary
# 06 Januari 2025

# Create Tuple (Immutable) tidak bisa .append .remove dll

list = []
tuple = (1, 2, 3)

print(tuple[1])
print("==================================================")

# Dictionary (key-value)

dictionary = {
    "name" : "Nanda",
    "age" : 22,
    "height" : 170,
    "married" : True,
}
dictionary["address"] = "Magelang"
dictionary.update({"color" : "blue", "country" : "India"})
dictionary.pop("married")
print(dictionary)
del dictionary["name"]
print(dictionary.get("name", "Not Found!"))
dictionary.clear() #Menghapus semua dictionary

print("==================================================")

# data_mahasiswa = {
#     '001' : {'name' : 'abdan', 'us': 40},
#     '033' : {'name' : 'fendy', 'us': 43},
# }
# print(data_mahasiswa['001']['name'])

data_mahasiswa = {
     '1231231' : {
        'name_student' : 'Fendy Orang Sukses',
        'nama_ortu' : {
            'father' : 'father horang kaya',
            'mother' : 'mother kaya banget',
            'nama_ortunya_ortu_gw' : {
                'grand_mother' : 'grand mother',
                'grand_father' : 'grand father',
            }
        }
    },
    '23324324' : {
        'name_student' : 'Nanda Orang Sukses',
        'nama_ortu' : {
            'father' : 'father horang kaya',
            'mother' : 'mother kaya banget',
        }
    }
}

print(data_mahasiswa['1231231']['nama_ortu']['mother'])
print(data_mahasiswa['1231231']['nama_ortu']['nama_ortunya_ortu_gw']['grand_mother'])
print(f"ID Mahasiswa {data_mahasiswa['1231231']}")

# .get


# hapus