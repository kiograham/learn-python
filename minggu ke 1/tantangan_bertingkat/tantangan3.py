
# 1. DATA MASUKAN DAN ATURAN BIAYA
biaya_tetap = 50000
konsumsi_per_orang = 12000

# 2. INPUT JUMLAH PESERTA
peserta = int(input("Banyak peserta: "))

# 3. VALIDASI DAN PROSES PERHITUNGAN
if peserta <= 0:
    print("Peserta harus lebih dari nol.")
else:
    konsumsi = peserta * konsumsi_per_orang
    total_biaya = biaya_tetap + konsumsi

    # 4. HASIL / OUTPUT
    print("\n=== RENCANA BIAYA KEGIATAN ===")
    print(f"Jumlah Peserta : {peserta} orang")
    print(f"Biaya Tetap    : Rp{biaya_tetap:,}".replace(",", "."))
    print(f"Biaya Konsumsi : Rp{konsumsi:,}".replace(",", "."))
    print(f"Total Biaya    : Rp{total_biaya:,}".replace(",", "."))
