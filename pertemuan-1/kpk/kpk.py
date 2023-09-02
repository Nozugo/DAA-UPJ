# KPK

"""
[ Algoritma ] 

1. Buat variabel x dan variabel y.
2. Masukkan 3 ke dalam variabel x dan 4 ke dalam variabel y.
3. Buat fungsi untuk mencari bilangan prima dari range yang telah ditentukan dengan cara menemukan bilangan yang hanya memiliki 2 faktor yaitu 1 dan bilangan itu sendiri.
4. Buat variabel prime_numbers dan masukkan list bilangan prima ke dalamnya dengan memanggil fungsi prime_number.
5. Buat fungsi untuk mencari faktor prima dari nilai variabel x dan nilai variabel y dengan membaginya menggunakan bilangan prima sampai faktornya tersisa bilangan prima saja. 
6. Buat variabel first_prime_faktor dan second_prime_factor. 
7. Masukkan faktor prima nilai variabel x ke dalam variabel first_prime_factor.
8. Masukkan faktor prima nilai variabel y ke dalam variabel second_prime_factor.
9. Buat fungsi untuk mencari KPK dengan cara mencari pangkat terbesar dari first_prime_faktor dan second_prime_factor.
10. Jika terdapat faktor prima yang sama dari variabel first_prime_factor dan second_prime_factor, maka cari pangkat yang paling besar diantara keduanya lalu masukkan ke dalam variabel result.
11. Jika faktor prima dari variabel first_prime_factor tidak sama dengan faktor prima dari variabel second_prima_factor, maka cek terlebih dahulu apakah faktor prima tersebut sudah ada di dalam variabel result atau belum. Jika tidak ada, maka masukkan ke variabel result, jika ada bandingkan dan masukkan pangkat yang paling besar.
12. Kalikan semua nilai yang ada di dalam variabel result dan tampilkan hasilnya ke layar.


[ Pseudocode ]

Function PrimeNumber(x)
    Prime ← []
    For i ← 1 to x
        Count ← 0
        If i == 1
            Continue
        For j ← 1 to x
            If i % j == 0
                Count ← Count + 1
        If Count == 2
            Append i to Prime
    Return Prime
EndFunction

Function PrimeFactor(x, prime_numbers)
    Factors ← {}

    For i in prime_numbers
        Count ← 0
        While x % i == 0
            x ← x / i
            Count ← Count + 1
            Factors[i] ← Count
    Return Factors
EndFunction

Function KPK(x, y)
    Result ← {}
    For i in x
        For j in y
            If i == j
                If x.Get(i) > y.Get(j)
                    Result[i] ← x.Get(i)
                Elif x.Get(i) < y.Get(j)
                    Result[j] ← y.Get(j)
                Elif x.Get(i) == y.Get(j)
                    Result[i] ← x.Get(i)
            Else
                If i in Result And Result.Get(i) > x.Get(i)
                    Continue
                Elif j in Result And Result.Get(j) > y.Get(j)
                    Continue
                Else
                    Result[i] ← x.Get(i)
                    Result[j] ← y.Get(j)
    Return Result
EndFunction

x ← 3
y ← 4

PrimeNumbers ← PrimeNumber(20)
FirstPrimeFactor ← PrimeFactor(x, PrimeNumbers)
SecondPrimeFactor ← PrimeFactor(y, PrimeNumbers)

Print(FirstPrimeFactor)
Print(SecondPrimeFactor)

Print()
Print(KPK(FirstPrimeFactor, SecondPrimeFactor))

PrimeKPK ← KPK(FirstPrimeFactor, SecondPrimeFactor)
ResultKPK ← 1
For i in PrimeKPK
    ResultKPK ← ResultKPK * i ^ PrimeKPK.Get(i)
EndFor

Print()
Print("KPK:", ResultKPK)

"""


def prime_number(x):
    prime = []
    for i in range(1, x+1):
        count = 0
        if i == 1:
            continue
        for j in range(1, x+1):
            if i % j == 0:
                count += 1
        if count == 2:
            prime.append(i)
    return prime


def prime_factor(x):
    faktor = {}

    for i in prime_numbers:
        count = 0
        while x % i == 0:
            x /= i
            count += 1
            faktor[i] = count
    return faktor


def kpk(x, y):
    result = {}
    for i in x:
        for j in y:
            if i == j:
                if x.get(i) > y.get(j):
                    result[i] = x.get(i)
                elif x.get(i) < y.get(j):
                    result[j] = y.get(j)
                elif x.get(i) == y.get(j):
                    result[i] = x.get(i)
            else:
                if i in result and result.get(i) > x.get(i):
                    continue
                elif j in result and result.get(j) > y.get(j):
                    continue
                else:
                    result[i] = x.get(i)
                    result[j] = y.get(j)
    return result


x = 3
y = 4

prime_numbers = prime_number(20)
first_prime_factor = prime_factor(x)
second_prime_factor = prime_factor(y)

print(first_prime_factor)
print(second_prime_factor)

print()
print(kpk(first_prime_factor, second_prime_factor))

prime_kpk = kpk(first_prime_factor, second_prime_factor)
result_kpk = 1
for i in prime_kpk:
    result_kpk = result_kpk * i ** prime_kpk.get(i)

print()
print(f"KPK: {result_kpk}")
