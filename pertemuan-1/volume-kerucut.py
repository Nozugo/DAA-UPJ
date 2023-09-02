# Volume Kerucut

"""
[ Algoritma ]

1. Import module Fraction untuk mengubah nilai desimal menjadi pecahan.
2. Buat variabel diameter, tinggi, r, dan pi.
3. Masukkan 5 ke dalam variabel diameter, 4 ke dalam variabel tinggi, dan 3.14 ke dalam variabel pi.
4. Menggunakan rumus (pi x r x r x t)/3 untuk menghitung volume kerucut.
5. Buat variabel v yang berisi hasil dari perhitungan (pi * r * r * tinggi) / 3.
6. Tampilkan nilai variabel v ke layar dan batasi bilangan di belakang koma sebanyak dua saja.
7. Tampilkan nilai variabel v ke layar berupa pecahan menggunakan fungsi yang terdapat pada module Fraction dan limit penyebutnya menggunakan method limit_denominator().

[ Pseudocode ]

Import Fraction as F from fractions

diameter ← 5
tinggi ← 4
r ← diameter / 2
pi ← 3.14

v ← (pi * r * r * tinggi) / 3

Print("[ Program Mencari Volume Kerucut ]")
Print("Diameter        : ", diameter)
Print("Jari-jari       : ", r)
Print("Tinggi          : ", tinggi)
Print("----------------------------------")
Print("Rumus           : (π * r * r * tinggi) / 3")
Print("Perhitungan     : (" + ToString(pi) + " * " + ToString(r) + " * " + ToString(r) + " * " + ToString(tinggi) + ") / 3")
Print("Hasil (Desimal) : " + ToString(v, 2))
Print("Hasil (Pecahan) : " + ToString(F(v).limit_denominator()))

"""

from fractions import Fraction as F

diameter = 5
tinggi = 4
r = diameter / 2
pi = 3.14

v = (pi * r * r * tinggi) / 3
print("[ Program Mencari Volume Kerucut ]")
print(f"Diameter    	: {diameter}")
print(f"Jari-jari   	: {r}")
print(f"Tinggi      	: {tinggi}")
print("----------------------------------")
print(f"Rumus       	: (π * r * r * tinggi) / 3")
print(f"Perhitungan 	: ({pi} * {r} * {r} * {tinggi}) / 3")
print(f"Hasil (Desimal) : {v:.2f}")
print(f"Hasil (Pecahan) : {F(v).limit_denominator()}")
