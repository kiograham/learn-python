berat_gram = int(input("Berat paket (gram): "))

if berat_gram <= 0:
    print("Berat harus positif.")
else:
    kg_tagihan = (berat_gram + 999) // 1000
    ongkir = kg_tagihan * 8000
    kemasan = 2000
    total = ongkir + kemasan
    
    print(f"Berat tertagih: {kg_tagihan} kg")
    print(f"Ongkir: Rp{ongkir}")
    print(f"Total dengan kemasan: Rp{total}")
