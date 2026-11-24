nama = input("Nama lengkap: ").strip()
nim = input("NIM: ").strip()
kelas = input("kelas: ").strip().upper()
lengkap = nama != "" and nim != "" and kelas != ""
if lengkap:
    print("KARTU PESERTA PRAKTIKUM")
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"Kelas: {kelas}")
else:
    print("Kartu belum dapat dibuat.")
    if nama == "":
        print("nama wajib diisi")
    if nim == "":
        print("NIM wajib diisi")
    if kelas == "":
        print("kelas wajib diisi")