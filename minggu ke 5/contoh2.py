aktif = input("Anggota aktif (ya/tidak): ").strip().lower()
terlambat = input("Ada keterlambatan (ya/tidak): ").strip().lower()
jumlah = int(input("Buku sedang dipinjam: "))
if aktif not in ("ya", "tidak") or terlambat not in ("ya", "tidak"):
         print("Jawaban harus ya atau tidak.")
elif jumlah < 0:
         print("Jumlah buku tidak valid.")
else:
    boleh = aktif == "ya" and terlambat == "tidak" and jumlah < 3
if boleh:
         print("Peminjaman diizinkan")
else:         
    print("Peminjaman ditolak")
    if aktif != "ya":
        print("Keanggotaan tidak aktif")         
    if terlambat == "ya":             
        print("Selesaikan keterlambatan")         
    if jumlah >= 3:             
        print("Batas pinjaman tercapai") 