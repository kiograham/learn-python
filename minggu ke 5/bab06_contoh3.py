# Contoh 3: Pola Segitiga Loop Bersarang
# Simpan sebagai bab06_contoh3.py
# Input contoh: 4

n = int(input("Tinggi segitiga (1-6): "))
if not 1 <= n <= 6:
    print("Tinggi harus 1 sampai 6")
else:
    cetak = 0
    for baris in range(1, n + 1):
        for kolom in range(1, baris + 1):
            print(kolom, end="")
            cetak += 1
        print()
    print(f"Jumlah angka tercetak: {cetak}")