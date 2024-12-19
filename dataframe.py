import pandas as pd


df_csv = pd.read_csv(r'C:\Users\ACER\OneDrive\Documents\semester 3\github\tugas dataframe\data_sampah.csv')


df_sampah = df_csv[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'satuan', 'tahun']]

print(df_sampah)


tahun_tertentu = 2023
total_produksi_tahun_tertentu = 0

for _, row in df_sampah.iterrows():
    if row['tahun'] == tahun_tertentu:
        total_produksi_tahun_tertentu += row['jumlah_produksi_sampah']

print(f"Jumlah produksi sampah di Jawa Barat pada tahun {tahun_tertentu}: {total_produksi_tahun_tertentu}")

# Hitung jumlah produksi per tahun
total_produksi_pertahun = {}

for _, row in df_sampah.iterrows():
    tahun = row['tahun']
    produksi = row['jumlah_produksi_sampah']
    total_produksi_pertahun[tahun] = total_produksi_pertahun.get(tahun, 0) + produksi

# Cetak hasil total produksi per tahun
for tahun, total in total_produksi_pertahun.items():
    print(f"Tahun {tahun}: {total}")


# Inisialisasi dictionary untuk menyimpan total produksi per Kota/Kabupaten per Tahun
produksi_per_kota_per_tahun = {}

# Hitung jumlah produksi sampah per Kota/Kabupaten per Tahun
for _, row in df_sampah.iterrows():
    
    key = (row['nama_kabupaten_kota'], row['tahun'])
    
    produksi_per_kota_per_tahun[key] = produksi_per_kota_per_tahun.get(key, 0) + row['jumlah_produksi_sampah']


for key, total in produksi_per_kota_per_tahun.items():
    print(f"Kota/Kabupaten: {key[0]}, Tahun: {key[1]}, Total Produksi Sampah: {total}")



