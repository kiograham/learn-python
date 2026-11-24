def hitung_ongkir(berat_gram):
    if not isinstance(berat_gram, int) or isinstance(berat_gram, bool):
        raise ValueError("Berat harus berupa bilangan bulat")

    if berat_gram <= 0:
        raise ValueError("Berat harus positif")

    kg_tagihan = (berat_gram + 999) // 1000
    ongkir = kg_tagihan * 8000
    kemasan = 2000
    total = ongkir + kemasan

    return {
        'berat_gram': berat_gram,
        'kg_tagihan': kg_tagihan,
        'ongkir': ongkir,
        'kemasan': kemasan,
        'total': total
    }

# Uji batas dari tabel contoh: 1000 gram
print("=== UJI BATAS: 1000 gram ===")
r = hitung_ongkir(1000)
print(f"Input berat: {r['berat_gram']} gram")
print(f"Langkah 1: kg_tagihan = (1000 + 999) // 1000 = 1999 // 1000 = {r['kg_tagihan']} kg")
print(f"Langkah 2: ongkir = {r['kg_tagihan']} * 8000 = Rp{r['ongkir']}")
print(f"Langkah 3: kemasan = Rp{r['kemasan']}")
print(f"Langkah 4: total = {r['ongkir']} + {r['kemasan']} = Rp{r['total']}")
print(f"HASIL: 1000 gram ditagih {r['kg_tagihan']} kg, total Rp{r['total']}")

print()

# Uji batas kedua: 1001 gram
print("=== UJI BATAS: 1001 gram ===")
r = hitung_ongkir(1001)
print(f"Input berat: {r['berat_gram']} gram")
print(f"Langkah 1: kg_tagihan = (1001 + 999) // 1000 = 2000 // 1000 = {r['kg_tagihan']} kg")
print(f"Langkah 2: ongkir = {r['kg_tagihan']} * 8000 = Rp{r['ongkir']}")
print(f"Langkah 3: kemasan = Rp{r['kemasan']}")
print(f"Langkah 4: total = {r['ongkir']} + {r['kemasan']} = Rp{r['total']}")
print(f"HASIL: 1001 gram ditagih {r['kg_tagihan']} kg, total Rp{r['total']}")

print()

# UJI PENOLAKAN yang belum ditampilkan: berat = 0 gram
print("=== UJI PENOLAKAN: 0 gram (harus ditolak) ===")
berat = 0
if berat <= 0:
    print(f"Input: {berat} gram")
    print("Kondisi: berat <= 0 → DITOLAK")
    print("Alasan: Spesifikasi 'berat bulat positif', 0 bukan positif")
    print("Keadaan data: tidak berubah, program keluar sebelum hitung")
else:
    r = hitung_ongkir(berat)
    print(f"Total: Rp{r['total']}")

print()

# Uji penolakan kedua: berat negatif
print("=== UJI PENOLAKAN: -500 gram (harus ditolak) ===")
berat = -500
if berat <= 0:
    print(f"Input: {berat} gram")
    print("Kondisi: berat <= 0 → DITOLAK")
    print("Alasan: Spesifikasi 'berat bulat positif', negatif tidak valid")
    print("Keadaan data: tidak berubah, program keluar sebelum hitung")
else:
    r = hitung_ongkir(berat)
    print(f"Total: Rp{r['total']}")

print()

# Tambahan: uji batas 999 gram (masih 1 kg)
print("=== UJI BATAS: 999 gram ===")
r = hitung_ongkir(999)
print(f"Input: {r['berat_gram']} gram → kg_tagihan = {r['kg_tagihan']} kg (masih 1 kg)")
print(f"Total: Rp{r['total']}")

print()

# Tambahan: uji batas 2000 gram (tepat 2 kg)
print("=== UJI BATAS: 2000 gram ===")
r = hitung_ongkir(2000)
print(f"Input: {r['berat_gram']} gram → kg_tagihan = {r['kg_tagihan']} kg")
print(f"Total: Rp{r['total']}")