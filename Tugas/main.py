from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilkanData


def main():
    data_mahasiswa = DataMahasiswa()
    

    while True:
        print("\nMenu Utama: ")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("6. Keluar")


        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
            jurusan_baru = input("Masukkan jurusan baru (kosongkan jika tidak ingin mengubah): ")
            data_mahasiswa.ubah_mahasiswa(nim, nama_baru or None, jurusan_baru or None)
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang akan dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            TampilkanData.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            TampilkanData.tampilkan_daftar(data_mahasiswa.mahasiswa_list)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

        
if __name__ == "__main__":
    main()
