import os
import csv
import traceback

# Path utama dataset
base_path = r'C:\Users\fauza\Documents\skripsi\WifiSensingDualReceiver\data\raw\dataset_scene3'
rx_folders = ['dataset RX 1', 'dataset RX 2']
activity_folders = ['BD', 'DD', 'JL']

# Nilai kolom ke-3 yang diperbolehkan
allowed_values = ['mac', '84:CC:A8:11:78:B1']
required_columns = 26  # jumlah kolom yang HARUS dimiliki per baris

for rx in rx_folders:
    for activity in activity_folders:
        folder_path = os.path.join(base_path, rx, activity)

        if not os.path.exists(folder_path):
            continue

        for file in os.listdir(folder_path):
            if file.endswith('.csv'):
                file_path = os.path.join(folder_path, file)

                try:
                    with open(file_path, 'r', newline='') as infile:
                        reader = csv.reader(infile)
                        filtered_rows = []

                        for row in reader:
                            if len(row) == required_columns and row[2] in allowed_values:
                                filtered_rows.append(row)

                    # Tulis ulang hasilnya
                    with open(file_path, 'w', newline='') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerows(filtered_rows)

                    print(f"Cleaned: {file_path}")

                except Exception as e:
                    print(f"Error processing {file_path}:\n{traceback.format_exc()}")
