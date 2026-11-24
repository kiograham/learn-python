harga = int(input("Harga per item: "))
jumlah = int(input("Jumlah item: "))

if harga < 0:
    print("Harga tidak boleh negatif.")
elif jumlah <= 0:
    print("Jumlah harus positif.")
else:
    subtotal = harga * jumlah
    kemasan = 2000
    total = subtotal + kemasan
    
    print(f"\nSubtotal: Rp{subtotal}")
    print(f"Biaya kemasan: Rp{kemasan}")
    print(f"Total: Rp{total}")