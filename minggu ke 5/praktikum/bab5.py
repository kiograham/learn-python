anggota = input("aktif (ya/tidak): ").strip().lower()
terlambat = input("terlambat (ya/tidak): ").strip().lower()
jumlah = int(input("jumlah buku dipinjam: "))

if anggota not in ("ya", "tidak") or terlambat not in ("ya", "tidak"):
    print("jawaban harus ya atau tidak")
elif jumlah < 0:
    print("jumlah buku tidak valid")
else:
    boleh = anggota == "ya" and terlambat == "tidak" and jumlah < 3
    if boleh:
        print("peminjaman diizinkan")
    else:
        print("peminjaman ditolak")
        if anggota != "ya":
            print("keanggotaan tidak aktif")
        if terlambat == "ya":
            print("selesaikan keterlambatan")
        if jumlah >= 3:
            print("batas pinjaman tercapai")