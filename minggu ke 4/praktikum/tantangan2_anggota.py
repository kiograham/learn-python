anggota = input("Anggota? (y/n): ").lower()
harga = int(input("Harga per item: "))
jumlah = int(input("Jumlah item: "))

if harga < 0:
    print("Harga tidak boleh negatif.")
elif jumlah <= 0:
    print("Jumlah harus positif.")
else:
    subtotal = harga * jumlah
    
    # Diskon hanya jika anggota DAN subtotal >= 100000
    if anggota == 'y' and subtotal >= 100000:
        diskon = subtotal * 0.05
    else:
        diskon = 0
    
    kemasan = 2000
    total = (subtotal - diskon) + kemasan
    
    print(f"\nSubtotal: Rp{subtotal}")
    print(f"Diskon (5%): Rp{diskon:.0f}")
    print(f"Biaya kemasan: Rp{kemasan}")
    print(f"Total: Rp{total}")