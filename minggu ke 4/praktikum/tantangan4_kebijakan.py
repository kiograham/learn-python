harga = int(input("Harga per item: "))
jumlah = int(input("Jumlah item: "))

if harga < 0:
    print("Harga tidak boleh negatif.")
elif jumlah <= 0:
    print("Jumlah harus positif.")
else:
    subtotal = harga * jumlah
    kemasan = 2000
    
    # Diskon 10% jika subtotal >= 100000
    persen_diskon = 0.10 if subtotal >= 100000 else 0.00
    
    # KEBIJAKAN A: Diskon pada subtotal saja
    diskon_A = subtotal * persen_diskon
    total_A = (subtotal - diskon_A) + kemasan
    
    # KEBIJAKAN B: Diskon pada (subtotal + kemasan)
    diskon_B = (subtotal + kemasan) * persen_diskon
    total_B = (subtotal + kemasan) - diskon_B
    
    print(f"\n=== PERBANDINGAN ===")
    print(f"Subtotal: Rp{subtotal}")
    print(f"Kemasan: Rp{kemasan}")
    print(f"Persentase diskon: {persen_diskon*100:.0f}%")
    print()
    print(f"--- Kebijakan A (diskon di subtotal) ---")
    print(f"Diskon: Rp{diskon_A:.0f}")
    print(f"Total: Rp{total_A:.0f}")
    print()
    print(f"--- Kebijakan B (diskon di subtotal+kemasan) ---")
    print(f"Diskon: Rp{diskon_B:.0f}")
    print(f"Total: Rp{total_B:.0f}")
    print()
    print(f"Selisih (B lebih murah): Rp{total_A - total_B:.0f}")
    print(f"  (Sama dengan kemasan * diskon = {kemasan} * {persen_diskon} = {kemasan * persen_diskon:.0f})")
