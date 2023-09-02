# Volume Tabung

"""
[ Algoritma ]

1. Buat variable r, tinggi, dan pi
2. Masukkan 3 ke dalam variabel r, 5 ke dalam variabel tinggi, dan 3.14 ke dalam variabel pi.
3. Menggunakan rumus pi * r * r * t untuk menghitung volume tabung.
4. Buat variable volume yang berisi hasil dari perhitungan r * r * tinggi * pi
5. Tampilkan nilai variabel volume ke layar.

[ Pseudocode ]

r ← 3
tinggi ← 5
pi ← 3.14
volume ← r * r * tinggi * pi

Print("[ Program Mencari Volume Tabung ]")
Print("Jari-jari   :", r)
Print("Tinggi      :", tinggi)
Print("π(pi)       :", pi)
Print("---------------------------------")
Print("Rumus       : πr²t")
Print("Perhitungan : " + ToString(pi) + " * " + ToString(r) + " * " + ToString(r) + " * " + ToString(tinggi))
Print("Hasil       :", volume)

"""

r = 3
tinggi = 5
pi = 3.14
volume = r * r * tinggi * pi
print("[ Program Mencari Volume Tabung ]")
print(f"Jari-jari   : {r}")
print(f"Tinggi  	: {tinggi}")
print(f"π(pi)   	: {pi}")
print("---------------------------------")
print(f"Rumus   	: πr²t")
print(f"Perhitungan : {pi} * {r} * {r} * {tinggi}")
print(f"Hasil   	: {volume}")
