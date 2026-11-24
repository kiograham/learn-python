harga = int(input("harga satuan (Rp): "))
jumlah = int(input("jumlah barang: "))
if harga <= 0 or jumlah <=0:
    print("Harga dan jumlah harus positif!!")
else:
    subtotal = harga * jumlah
    diskon = 0
    if subtotal >= 100000:
        diskon = subtotal * 10 // 100
    bayar = subtotal - diskon 
    print(f"subtotal: Rp{subtotal}")
    print(f"diskon: Rp{diskon}")
    print(f"total bayar: Rp{bayar}")