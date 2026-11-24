biaya_tetap = 50000
konsumsi_per_orang = 12000
peserta = int(input("Banyak peserta: "))
if peserta <= 0:
    print("Peserta harus lebih dari nol.")
else: 
    konsumsi = peserta * konsumsi_per_orang
    total_biaya = biaya_tetap + konsumsi
    print(f"Peserta: {peserta}")
    print(f"Biaya Tetap: Rp{biaya_tetap}")
    print(f"Konsumsi: Rp{konsumsi}")
    print(f"Total Biaya: Rp{total_biaya}")