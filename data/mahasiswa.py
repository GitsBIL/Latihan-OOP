class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"ID: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"

class DataMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_data(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)

    def hapus_data(self, nim):
        self.mahasiswa_list = [m for m in self.mahasiswa_list if m.nim != nim]

    def ubah_data(self, nim, nama=None, jurusan=None):
        for m in self.mahasiswa_list:
            if m.nim == nim:
                if nama: m.nama = nama
                if jurusan: m.jurusan = jurusan
                if umur: m.umur = umur

    def cari_data(self, nim):
        for m in self.mahasiswa_list:
            if m.nim == nim:
                return m
        return None
