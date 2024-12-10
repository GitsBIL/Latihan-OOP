from data import Mahasiswa, DataMahasiswa
from view import InputForm, MahasiswaView

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Input Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Tampilkan Detail Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Ubah Data Mahasiswa")
        print("6. Keluar")
        
        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            input_form = InputForm(data_mahasiswa)
            input_form.input_data()
        elif choice == "2":
            mahasiswa_view = MahasiswaView(data_mahasiswa)
            mahasiswa_view.tampilkan_data()
        elif choice == "3":
            nim = input("Masukkan NIM untuk melihat detail: ")
            mahasiswa_view = MahasiswaView(data_mahasiswa)
            mahasiswa_view.tampilkan_detail(nim)
        elif choice == "4":
            nim = input("Masukkan NIM untuk dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
            print("Data mahasiswa berhasil dihapus.")
        elif choice == "5":
            nim = input("Masukkan NIM untuk diubah: ")
            nama_baru = input("Masukkan Nama Baru: ")
            data_mahasiswa.ubah_mahasiswa(nim, nama_baru)
            print("Data mahasiswa berhasil diubah.")
        elif choice == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
