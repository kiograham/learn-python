print("=" *40)
nama = input("masukkan nama lengkap anda: ").strip()
nim = int(input("masukkan NIM anda: ").strip())
kelas = input("masukkan kelas anda: ").strip()
kota = input("masukkan kota asal anda: ").strip()
print("=" *40)

if nama == "" or nim == 0 or kelas == "" or kota == "":
    print("Data wajib diisi")
    if nama == "":
        print("nama wajib diisi")
    if nim == 0:
        print("NIM wajib diisi")
    if kelas == "":
        print("kelas wajib diisi")
    if kota == "":
        print("kota asal wajib diisi")
else:
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"Kelas: {kelas}")
    print(f"Kota asal: {kota}")