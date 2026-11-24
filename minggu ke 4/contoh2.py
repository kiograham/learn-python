tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

valid = (0 <= tugas <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100)

if not valid:
    print("Seluruh nilai harus 0 sampai 100.")
else:
    komponen_tugas = tugas * 0.30
    komponen_uts = uts * 0.30
    komponen_uas = uas * 0.40
    akhir = komponen_tugas + komponen_uts + komponen_uas
    
    print(f"Komponen: {komponen_tugas:.2f}, "
           f"{komponen_uts:.2f}, {komponen_uas:.2f}")
    print(f"Nilai akhir: {akhir:.2f}")

