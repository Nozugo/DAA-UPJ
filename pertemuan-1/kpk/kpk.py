# KPK

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

print(f"Bilangan pertama : {x}")
print(f"Bilangan kedua   : {y}")

prime_kpk = kpk(first_prime_factor, second_prime_factor)
result_kpk = 1
for i in prime_kpk:
    result_kpk = result_kpk * i ** prime_kpk.get(i)

print()
print(f"KPK: {result_kpk}")
