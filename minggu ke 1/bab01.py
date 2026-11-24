nama = input("nama: ").strip()
prodi = input("program studi: ").strip()
if nama == "" or prodi == "":
    print("Nama dan program studi wajib diisi.")
else: 
    print(f"Halo {nama}!")
    print(f"profil: {nama} | {prodi}") 