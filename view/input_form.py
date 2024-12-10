class InputForm:
    def input_data(self):
        print("Masukkan Data Mahasiswa:")
        id = input("NIM: ")
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        return id, nama, jurusan
