tempat = input("Tujuan (perpustakaan/laboratorium): ").strip().lower()

if tempat == "perpustakaan":
    aksi = input("Aksi (baca/diskusi): ").strip().lower()
    if aksi == "baca":
        print("Anda menemukan referensi algoritma.")
    elif aksi == "diskusi":
        print("Anda menyusun rencana bersama teman.")
    else:
        print("Aksi perpustakaan tidak valid.")
elif tempat == "laboratorium":
    aksi = input("Aksi (kode/uji): ").strip().lower()
    if aksi == "kode":
        print("Anda membangun prototipe.")
    elif aksi == "uji":
        print("Anda menemukan sebuah bug.")
    else:
        print("Aksi laboratorium tidak valid.")
else:
    print("Tujuan tidak valid.")