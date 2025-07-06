import os

# --- KONFIGURASI UTAMA ---
base_folder = r'C:\Users\Hp\Documents\SKRIPSI !!!!!\TA\TA_saya\dataset\Dataset_scene1'
subfolders = ['dataset RX 1', 'dataset RX 2']
# --- SELESAI KONFIGURASI ---

def rename_multiple_batches(direktori):
    print(f"\n=== Mulai Rename di: {os.path.abspath(direktori)} ===")
    
    # Batch 1: data1.csv - data15.csv  -> JL_1.csv - JL_15.csv
    for i in range(1, 16): 
        old_name = f"data{i}.csv"
        new_name = f"JL_{i}.csv"
        _rename_file(direktori, old_name, new_name)

    # Batch 2: data16.csv - data30.csv -> DD_1.csv - DD_15.csv
    for i in range(1, 16): 
        old_name = f"data{15 + i}.csv"
        new_name = f"DD_{i}.csv"
        _rename_file(direktori, old_name, new_name)

    # Batch 3: data31.csv - data45.csv -> BD_1.csv - BD_15.csv
    for i in range(1, 16): 
        old_name = f"data{30 + i}.csv"
        new_name = f"BD_{i}.csv"
        _rename_file(direktori, old_name, new_name)

def _rename_file(folder, old_name, new_name):
    path_lama = os.path.join(folder, old_name)
    path_baru = os.path.join(folder, new_name)

    if os.path.exists(path_lama):
        try:
            os.rename(path_lama, path_baru)
            print(f"✓ {old_name} → {new_name}")
        except Exception as e:
            print(f"✗ Gagal rename {old_name} → {new_name}: {e}")
    else:
        print(f"⚠ File tidak ditemukan: {old_name}")

if __name__ == "__main__":
    for subfolder in subfolders:
        full_path = os.path.join(base_folder, subfolder)
        rename_multiple_batches(full_path)
