total = 0
jumlah = 0

while True:
    skor = int(input("Skor 0-100 (-1 selesai): "))
    
    if skor == -1:
        break
    
    if skor < 0 or skor > 100:
        print("Skor ditolak")
        print(f"Jumlah valid: {jumlah} total: {total}")
        continue
    
    total += skor
    jumlah += 1
    print(f"Jumlah valid: {jumlah} total: {total}")

if jumlah > 0:
    print(f"Rata-rata: {total / jumlah:.2f}")
else:
    print("Belum ada skor valid")