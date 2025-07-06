import os

# --- KONFIGURASI UTAMA ---
base_folder = r'C:\Users\Hp\Documents\SKRIPSI !!!!!\TA\TA_saya\dataset\Dataset_scene2'
subfolders = ['dataset RX 1', 'dataset RX 2']
# --- SELESAI KONFIGURASI ---

def rename_multiple_batches(direktori):
    print(f"\n=== Mulai Rename di: {os.path.abspath(direktori)} ===")

    batch_configs = [
        (46, 60, "JL", 1),   # data46–60 → JL_1–15
        (61, 75, "DD", 1),   # data61–75 → DD_1–15
        (76, 90, "BD", 1),   # data76–90 → BD_1–15
    ]

    for start, end, prefix, suffix_start in batch_configs:
        print(f"\n-- Batch {prefix}: data{start}.csv to data{end}.csv → {prefix}_{suffix_start}.csv ...")
        for i, number in enumerate(range(start, end + 1)):
            old_name = f"data{number}.csv"
            new_name = f"{prefix}_{suffix_start + i}.csv"
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
