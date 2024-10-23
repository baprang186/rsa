from math import isqrt
from fractions import Fraction

# Ham tinh phan so lien tuc cua mot phan so
def continued_fraction(numerator, denominator):
    result = []
    while denominator:
        q = numerator // denominator
        result.append(q)
        numerator, denominator = denominator, numerator - q * denominator
    return result

# Ham tinh xap xi lien tiep cua phan so lien tuc
def convergents(continued_fraction):
    convergents = []
    for i in range(len(continued_fraction)):
        frac = Fraction(continued_fraction[i], 1)
        for j in range(i - 1, -1, -1):
            frac = continued_fraction[j] + 1 / frac
        convergents.append(frac)
    return convergents

# Ham kiem tra xem k/d co phai la khoa bi mat dung hay khong
def wiener_attack(e, n):
    frac = continued_fraction(e, n)
    converg = convergents(frac)

    for k_d in converg:
        if k_d.denominator == 0:
            continue
        d = k_d.denominator
        k = k_d.numerator

        if k == 0:
            continue

        # Tinh toan phi(n) tu d va e
        phi_n = (e * d - 1) // k

        # Giai phuong trinh bac 2 de tim p va q
        a = 1
        b = -(n - phi_n + 1)
        c = n
        discriminant = b * b - 4 * a * c

        if discriminant >= 0:
            sqrt_disc = isqrt(discriminant)
            if sqrt_disc * sqrt_disc == discriminant:
                p = (-b + sqrt_disc) // (2 * a)
                q = (-b - sqrt_disc) // (2 * a)
                if p * q == n:
                    return d

    return None

# Vi du RSA bi tan cong
e = 17993
n = 90581
d = wiener_attack(e, n)

if d:
    print("Tim thay khoa bi mat d:", d)
else:
    print("Khong tim thay khoa bi mat.")
