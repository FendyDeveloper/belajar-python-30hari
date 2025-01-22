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

        for list_names, list_nims in zip(list_of_students, list_of_nim_students):
            print(f"{list_nims.strip()} : {list_names.strip()}")

        print(f'Data students berhasil ditampilkan!')

    def update_student(self, nim):
        names = open(self.name_file, 'r')
        nims = open(self.nim_file, 'r')
        list_names = names.readlines()
        list_nims = nims.readlines()
        for idx, cek_nim in enumerate(list_nims):
            if nim == cek_nim.strip():
                print(f"NIM {nim} ditemukan")
                new_name = input("Masukkan nama baru: ")
                list_names[idx] = new_name + '\n'
                break
        with open(self.name_file, 'w') as name_file:
            name_file.writelines(list_names)

        names.close()
        nims.close()

    def delete_student(self, nim):
        with open(self.nim_file, 'r') as nim_file, open(self.name_file, 'r') as name_file:
            name_lists = name_file.readlines()
            nim_lists = nim_file.readlines()

        for idx, cek_nim in enumerate(nim_lists):
            if nim == cek_nim.strip():
                print(f"NIM {nim} Berhasil dihapus")
                del nim_lists[idx]
                del name_lists[idx]
                break

        with open(self.name_file, 'w') as name_file, open(self.nim_file, 'w') as nim_file:
            name_file.writelines(name_lists)
            nim_file.writelines(nim_lists)

db = DatabaseStudents()
choice_data = True

while choice_data:
    print("CRUD Data Mahasiswa".center(50, '-'))
    print("1. Show All Data Students")
    print("2. Add Data Students")
    print("3. Update Data Students")
    print("4. Delete Data Students")
    input_choice = input("Enter your choice: ")
    if input_choice == '1':
        db.show_all_students()
        choice_data_input = True
        while choice_data_input:
            cek_data = input("Cek data lainnya? (y/n) : ")
            if cek_data.lower() == 'y':
                choice_data = True
                break
            elif cek_data.lower() == 'n':
                choice_data = False
                break
            else:
                choice_data = True
                break
    elif input_choice == '2':
        nama = input("Nama: ")
        nim = input("NIM: ")
        db.add_student(nama, nim)
        choice_data_input = True
        while choice_data_input:
            cek_data = input("Cek data lainnya? (y/n) : ")
            if cek_data.lower() == 'y':
                choice_data = True
                break
            elif cek_data.lower() == 'n':
                choice_data = False
                break
            else:
                choice_data = True
                break
    elif input_choice == '3':
        nim = input("NIM: ")
        db.update_student(nim)
        choice_data_input = True
        while choice_data_input:
            cek_data = input("Cek data lainnya? (y/n) : ")
            if cek_data.lower() == 'y':
                choice_data = True
                break
            elif cek_data.lower() == 'n':
                choice_data = False
                break
            else:
                choice_data = True
                break
    elif input_choice == '4':
        nim = input("NIM: ")
        db.delete_student(nim)
        choice_data_input = True
        while choice_data_input:
            cek_data = input("Cek data lainnya? (y/n) : ")
            if cek_data.lower() == 'y':
                choice_data = True
                break
            elif cek_data.lower() == 'n':
                choice_data = False
                break
            else:
                choice_data = True
                break


