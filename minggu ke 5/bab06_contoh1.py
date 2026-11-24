# Contoh 1: Game Tebak Angka
# Simpan sebagai bab06.py
# Input contoh: 4 9 7

rahasia = 7
batas = 3
percobaan = 0
menang = False

while percobaan < batas:
    tebakan = int(input("Tebak angka 1-10: "))
    percobaan += 1
    if tebakan == rahasia:
        menang = True
        break
    elif tebakan < rahasia:
        print("Terlalu kecil")
    else:
        print("Terlalu besar")
    print(f"Percobaan: {percobaan}")

if not menang:
    print(f"Jawaban: {rahasia}")