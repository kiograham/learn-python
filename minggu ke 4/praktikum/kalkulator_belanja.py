# Kalkulator Belanja
# ==================

print("=" *40)
harga = int(input("Harga per item (bulat): "))
jumlah = int(input("Jumlah item: "))
print("=" *40)

if harga < 0:
    print("Harga tidak boleh negatif.")
elif jumlah <= 0:
    print("Jumlah harus positif.")
else:
    subtotal = harga * jumlah
    
    if subtotal >= 50000:
        diskon = subtotal * 0.05
    else:
        diskon = 0
    
    total = (subtotal - diskon) + 2000
    
    print(f"\nSubtotal: Rp{subtotal}")
    print(f"Diskon (5%): Rp{diskon:.0f}")
    print(f"Total: Rp{total}")