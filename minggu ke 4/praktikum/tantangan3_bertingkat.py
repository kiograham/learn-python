harga = int(input("Harga per item: "))
jumlah = int(input("Jumlah item: "))

if harga < 0:
    print("Harga tidak boleh negatif.")
elif jumlah <= 0:
    print("Jumlah harus positif.")
else:
    subtotal = harga * jumlah
    
    # Diskon bertingkat - hanya yang paling tinggi
    if subtotal >= 100000:
        diskon = subtotal * 0.10 #10 persen
    elif subtotal >= 50000:
        diskon = subtotal * 0.05 #5 persen
    else:
        diskon = 0
    
    kemasan = 2000
    total = (subtotal - diskon) + kemasan
    
    print(f"\nSubtotal: Rp{subtotal}")
    print(f"Diskon: Rp{diskon:.2f}")
    print(f"Biaya kemasan: Rp{kemasan}")
    print(f"Total: Rp{total:.2f}")
