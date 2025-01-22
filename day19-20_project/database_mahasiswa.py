class DatabaseStudents:
    def __init__(self, name_file = 'name_file.txt', nim_file = 'nim_file.txt'):
        self.name_file = name_file
        self.nim_file = nim_file

        file1 = open(self.name_file, 'a')
        file2 = open(self.nim_file, 'a')
        file1.close()
        file2.close()

    def add_student(self, name, nim):

        with open(self.nim_file, 'r') as nim_file:
            nim_lists = nim_file.readlines()

        for existing_nim in nim_lists:
            if nim == existing_nim.strip():
                print(f"Nim {nim.strip()} already exists")
                return

        with open(self.name_file, 'a') as name_file, open(self.nim_file, 'a') as nim_file:
            name_lists = name_file.write(name + "\n")
            nim_lists = nim_file.write(nim + "\n")

        print(f"Nim {nim.strip()} added")
        print(f"Name {name.strip()} added")



    def show_all_students(self):
        name = open(self.name_file, 'r')
        nim = open(self.nim_file, 'r')
        list_of_students = name.readlines()
        list_of_nim_students = nim.readlines()
        # for list_name in list_of_students:
        #     list_names = list_name.strip()
        #     print(f"Name : {list_names}")
        # for list_nim in list_of_nim_students:
        #     list_nims = list_nim.strip()
        #     print(f"Nim : {list_nims}")

        for list_names, list_nims in zip(list_of_students, list_of_nim_students):
            print(f"{list_nims.strip()} : {list_names.strip()}")

        print(f'Data students berhasil ditampilkan!')

    def update_student(self, name, nim):
        # self.name = name
        # self.nim = nim

        # name = open(self.name_file, 'r')
        nims = open(self.nim_file, 'r')
        # list_of_names = name.readlines()
        list_nims = nims.readlines()
        print(list_nims)
        for len_nims in range(len(list_nims)):
            cek_nim = list_nims[len_nims].strip()
            if nim == cek_nim.strip():
                print("Nim ditemukan")
                new_name = input("Masukan nama baru: ")
                list_nims[len_nims] = new_name + '\n'
                break
        with open(self.name_file, 'w') as name_file:
            name_file.writelines(list_nims)





db = DatabaseStudents()
# db.add_student('Fendy2', '13')
db.show_all_students()
db.update_student('Fendy2', '13')