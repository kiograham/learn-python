skor = 0
print("1. Struktur LIFO adalah a) stack b) queue")
jawab = input("Jawaban: ").strip().lower() 
if jawab == "a":
    skor += 10
    print("jawaban benar")
elif jawab == "b":
    skor += 0
    print("jawaban salah")
else :
    print("masukkan jawaban yang benar (a/b)")
print("2. Hasil 7 % 3 adalah a) 2b) 1")
jawab = input("jawaban: ").strip().lower()
if jawab == "a":
    skor += 10
    print("jawaban benar")
elif jawab == "b":
    skor += 0
    print("jawaban salah")
else:
    print("masukkan jawaban yang benar (a/b)")
print(f"skor akhir: {skor}/20")