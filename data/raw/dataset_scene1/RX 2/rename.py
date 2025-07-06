import os

# --- KONFIGURASI ---
# Ganti dengan path ke direktori tempat file CSV Anda berada.
# Contoh: 'C:/Users/NamaAnda/Documents/FileCSV' atau '/home/namaanda/dokumen/filecsv'
# Jika skrip ini berada di folder yang sama dengan file CSV, cukup gunakan '.'
direktori_csv = '.' 
# --- SELESAI KONFIGURASI ---

def rename_multiple_batches(direktori):
    print(f"Mencoba me-rename file di direktori: {os.path.abspath(direktori)}")
    print("Skrip ini mengasumsikan nama file asli adalah 'data1.csv' hingga 'data45.csv'.")
    print("Pastikan tidak ada spasi di awal nama file sumber maupun nama file target yang diinginkan.")
    
    print("\nPola rename yang akan dilakukan:")
    print("1. data1.csv  - data15.csv  -> JL_1.csv  - JL_15.csv")
    print("2. data16.csv - data30.csv -> DD_1.csv  - DD_15.csv")
    print("   (CATATAN: Untuk batch kedua, penamaan adalah DD_1, DD_2, ..., DD_15)")
    print("3. data31.csv - data45.csv -> BD_1.csv  - BD_15.csv")

    konfirmasi = input(f"\nLanjutkan dengan proses rename ini di direktori '{os.path.abspath(direktori)}'? (y/n): ").lower()
    if konfirmasi != 'y':
        print("Proses rename dibatalkan.")
        return

    print("\nMemulai proses rename...")
    overall_success = True # Akan menjadi False jika ada file sumber yang tidak ditemukan atau gagal di-rename
    files_found_and_processed = 0 # Menghitung berapa banyak file sumber yang ditemukan dan diproses

    # Batch 1: data1.csv - data15.csv  -> JL_1.csv - JL_15.csv
    print("\n--- Batch 1: data -> JL ---")
    for i in range(1, 16): 
        original_file_number = i
        nama_file_lama = f"data{original_file_number}.csv"
        nama_file_baru = f"JL_{i}.csv"
        path_lama = os.path.join(direktori, nama_file_lama)
        path_baru = os.path.join(direktori, nama_file_baru)

        if os.path.exists(path_lama):
            files_found_and_processed +=1
            try:
                os.rename(path_lama, path_baru)
                print(f"Berhasil: '{nama_file_lama}' -> '{nama_file_baru}'")
            except FileExistsError:
                print(f"Gagal: File tujuan '{nama_file_baru}' sudah ada. Lewati '{nama_file_lama}'.")
                overall_success = False
            except OSError as e:
                print(f"Gagal me-rename '{nama_file_lama}': {e}")
                overall_success = False
        else:
            print(f"Peringatan: File sumber '{nama_file_lama}' untuk batch JL tidak ditemukan.")
            overall_success = False # File sumber yang diharapkan tidak ada

    # Batch 2: data16.csv - data30.csv -> DD_1.csv - DD_15.csv
    print("\n--- Batch 2: data -> DD ---")
    for i in range(1, 16): 
        original_file_number = 15 + i # Ini akan menghasilkan angka 16 sampai 30
        nama_file_lama = f"data{original_file_number}.csv"
        nama_file_baru = f"DD_{i}.csv" # Nama baru tetap menggunakan suffix 1 sampai 15
        path_lama = os.path.join(direktori, nama_file_lama)
        path_baru = os.path.join(direktori, nama_file_baru)

        if os.path.exists(path_lama):
            files_found_and_processed +=1
            try:
                os.rename(path_lama, path_baru)
                print(f"Berhasil: '{nama_file_lama}' -> '{nama_file_baru}'")
            except FileExistsError:
                print(f"Gagal: File tujuan '{nama_file_baru}' sudah ada. Lewati '{nama_file_lama}'.")
                overall_success = False
            except OSError as e:
                print(f"Gagal me-rename '{nama_file_lama}': {e}")
                overall_success = False
        else:
            print(f"Peringatan: File sumber '{nama_file_lama}' untuk batch DD tidak ditemukan.")
            overall_success = False

    # Batch 3: data31.csv - data45.csv -> BD_1.csv - BD_15.csv
    print("\n--- Batch 3: data -> BD ---")
    for i in range(1, 16): 
        original_file_number = 30 + i # Ini akan menghasilkan angka 31 sampai 45
        nama_file_lama = f"data{original_file_number}.csv"
        nama_file_baru = f"BD_{i}.csv" # Nama baru tetap menggunakan suffix 1 sampai 15
        path_lama = os.path.join(direktori, nama_file_lama)
        path_baru = os.path.join(direktori, nama_file_baru)

        if os.path.exists(path_lama):
            files_found_and_processed +=1
            try:
                os.rename(path_lama, path_baru)
                print(f"Berhasil: '{nama_file_lama}' -> '{nama_file_baru}'")
            except FileExistsError:
                print(f"Gagal: File tujuan '{nama_file_baru}' sudah ada. Lewati '{nama_file_lama}'.")
                overall_success = False
            except OSError as e:
                print(f"Gagal me-rename '{nama_file_lama}': {e}")
                overall_success = False
        else:
            print(f"Peringatan: File sumber '{nama_file_lama}' untuk batch BD tidak ditemukan.")
            overall_success = False
            
    # Ringkasan hasil akhir
    if files_found_and_processed == 0:
        print("\nTidak ada file 'dataX.csv' yang relevan (data1.csv - data45.csv) yang ditemukan untuk diproses.")
    elif overall_success : # Hanya jika semua operasi yang DIHARAPKAN (file sumber ada & rename berhasil) sukses
        print("\nSemua file yang ditemukan dan ditentukan berhasil di-rename sesuai batch.")
    else: # Jika ada file sumber yang tidak ditemukan ATAU ada error saat rename
        print("\nBeberapa file tidak ditemukan atau gagal di-rename. Harap periksa log di atas.")

if __name__ == "__main__":
    rename_multiple_batches(direktori_csv)