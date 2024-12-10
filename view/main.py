from data import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def main():
    data_mahasiswa = DataMahasiswa()
    input_form = InputForm()
    mahasiswa_view = MahasiswaView()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Ubah Data Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            id, nama, jurusan = input_form.input_data()  # Hilangin input umur
            mahasiswa = Mahasiswa(id, nama, jurusan)  # Hilangin umur
            data_mahasiswa.tambah_data(mahasiswa)
            print("Data mahasiswa berhasil ditambahkan!")

        elif pilihan == "2":
            mahasiswa_view.tampilkan_list(data_mahasiswa.mahasiswa_list)

        elif pilihan == "3":
            id = input("Masukkan ID Mahasiswa yang ingin dicari: ")
            mahasiswa = data_mahasiswa.cari_data(id)
            mahasiswa_view.tampilkan_detail(mahasiswa)

        elif pilihan == "4":
            id = input("Masukkan ID Mahasiswa yang ingin dihapus: ")
            data_mahasiswa.hapus_data(id)
            print("Data mahasiswa berhasil dihapus!")

        elif pilihan == "5":
            id = input("Masukkan ID Mahasiswa yang ingin diubah: ")
            nama = input("Nama Baru (kosongkan untuk tidak mengubah): ")
            jurusan = input("Jurusan Baru (kosongkan untuk tidak mengubah): ")

            data_mahasiswa.ubah_data(id, nama if nama else None, jurusan if jurusan else None)
            print("Data mahasiswa berhasil diubah!")

        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
