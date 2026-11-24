def hitung_versi_lama(tugas, uts, uas):
    """Versi lama: pembulatan setiap komponen"""
    kt = round(tugas * 0.30, 2)
    ku = round(uts * 0.30, 2)
    kua = round(uas * 0.40, 2)
    akhir = kt + ku + kua
    return kt, ku, kua, akhir

def hitung_versi_baru(tugas, uts, uas):
    """Versi baru: TANPA pembulatan per komponen"""
    kt = tugas * 0.30
    ku = uts * 0.30
    kua = uas * 0.40
    akhir = kt + ku + kua
    return kt, ku, kua, akhir

# Input
tugas = float(input("Nilai tugas (0-100): "))
uts = float(input("Nilai UTS (0-100): "))
uas = float(input("Nilai UAS (0-100): "))

if not (0 <= tugas <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
    print("Semua nilai harus 0-100.")
else:
    # Hitung kedua versi
    kt_lama, ku_lama, kua_lama, akhir_lama = hitung_versi_lama(tugas, uts, uas)
    kt_baru, ku_baru, kua_baru, akhir_baru = hitung_versi_baru(tugas, uts, uas)
    
    print(f"\n=== VERSI LAMA (pembulatan per komponen) ===")
    print(f"Komponen: {kt_lama:.2f}, {ku_lama:.2f}, {kua_lama:.2f}")
    print(f"Nilai akhir: {akhir_lama:.2f}")
    
    print(f"\n=== VERSI BARU (tanpa pembulatan per komponen) ===")
    print(f"Komponen: {kt_baru:.4f}, {ku_baru:.4f}, {kua_baru:.4f}")
    print(f"Nilai akhir: {akhir_baru:.2f}")
    
    print(f"\n=== PERBEDAAN ===")
    print(f"Selisih nilai akhir: {abs(akhir_lama - akhir_baru):.4f}")
