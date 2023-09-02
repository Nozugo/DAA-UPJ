# Luas Segitiga

"""

[ Algoritma ]

1. Buat variable alas dan tinggi.
2. Masukkan 25 ke dalam variabel alas dan 30 ke dalam variabel tinggi.
3. Menggunakan rumus (alas * tinggi) / 2 untuk menghitung luas segitiga.
4. Buat variabel luas yang berisi hasil dari perhitungan (alas * tinggi) // 2.
5. Tampilkan nilai variabel luas ke layar.

[ Pseudocode ]

alas ← 25
tinggi ← 30
luas ← (alas * tinggi) // 2

Print("[ Program Mencari Luas Segitiga ]")
Print("Alas         :", alas)
Print("Tinggi       :", tinggi)
Print("--------------------------------")
Print("Rumus        : (alas * tinggi) / 2")
Print("Perhingungan : (" + ToString(alas) + " * " + ToString(tinggi) + ") / 2")
Print("Hasil        :", luas)

"""

alas = 25
tinggi = 30
luas = (alas * tinggi) // 2
print("[ Program Mencari Luas Segitiga ]")
print(f"Alas         : {alas}")
print(f"Tinggi       : {tinggi}")
print("--------------------------------")
print(f"Rumus        : (alas * tinggi) / 2")
print(f"Perhingungan : ({alas} * {tinggi}) / 2")
print(f"Hasil        : {luas}")
