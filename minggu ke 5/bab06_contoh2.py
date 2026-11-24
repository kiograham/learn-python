# Contoh 2: Akumulasi Skor dan Sentinel (versi buku)
# Simpan sebagai bab06_contoh2.py

total = 0
jumlah = 0

skor = int(input("Skor 0-100 (-1 selesai): "))

if skor == -1:
    print("Belum ada skor valid")
else:
    while skor != -1:
        if skor < 0 or skor > 100:
            print("Skor ditolak")
        else:
            total += skor
            jumlah += 1
        skor = int(input("Skor 0-100 (-1 selesai): "))

    if jumlah > 0:
        print(f"Rata-rata: {total / jumlah:.2f}")
    else:
        print("Belum ada skor valid")