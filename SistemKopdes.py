# import ini jangan dihapus/diedit yak
import random


def totalPenjualan(data, n):
    # kerjakan di sini
    if n == 0:
        return 0
    else:
        return data[0][1] + totalPenjualan(data[1:], n - 1)
    

def penjualanTertinggi(data, n):
    # kerjakan di sini
    if n == 1:
        return data[0]
    
    tersis = penjualanTertinggi(data[1:], n - 1)
    if data[0][1] > tersis[1]:
        return data[0]
    else:
        return tersis


def diAtasRataRata(penjualan, rataRata):
    # kerjakan di sini
    hit  = 0
    for ko in penjualan.values():
        if ko > rataRata:
            hit += 1
    return hit


# Program Utama - Jangan dihapus/diedit yak
angka = int(input("NIM: "))
random.seed(angka)

barang = [
    "Beras",
    "Minyak",
    "Gula",
    "Telur",
    "Kopi",
    "Teh"
]

penjualan = {}

for namaBarang in barang:
    penjualan[namaBarang] = random.randint(100, 500)

data = list(penjualan.items())
n = len(data)

print("\n===== Data Penjualan =====")
for namaBarang, jumlah in penjualan.items():
    print(namaBarang, ":", jumlah)

total = totalPenjualan(data, n)
tertinggi = penjualanTertinggi(data, n)
rataRata = total / n
jumlahDiAtasRataRata = diAtasRataRata(penjualan, rataRata)
print()
print(data)
print()
print("\n===== Hasil Analisis =====")
print("Total penjualan        :", total)
print("Penjualan tertinggi    :", tertinggi[0], "(", tertinggi[1], ")")
print("Rata-rata penjualan    :", round(rataRata, 2))
print("Di atas rata-rata      :", jumlahDiAtasRataRata, "barang")