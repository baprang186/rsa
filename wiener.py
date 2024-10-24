from math import isqrt
from fractions import Fraction

# Hàm tính phân số liên tục của một phân số
def continued_fraction(numerator, denominator):
    result = []
    while denominator:
        q = numerator // denominator
        result.append(q)
        numerator, denominator = denominator, numerator - q * denominator
    return result

# Hàm tính xấp xỉ liên tiếp của phân số liên tục
def convergents(continued_fraction):
    convergents = []
    for i in range(len(continued_fraction)):
        frac = Fraction(continued_fraction[i], 1)
        for j in range(i - 1, -1, -1):
            frac = continued_fraction[j] + 1 / frac
        convergents.append(frac)
    return convergents

# Hàm kiểm tra xem k/d có phải là khóa bí mật đúng hay không
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

        # Tính toán phi(n) từ d và e
        phi_n = (e * d - 1) // k

        # Giải phương trình bậc hai để tìm p và q
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

# Ví dụ RSA bị tấn công
#e = 17993
#n = 90581
e=int(input("Nhap e:"))
n=int(input("Nhap n:"))
d = wiener_attack(e, n)

if d:
    print(f"Tìm thấy khóa bí mật d: {d}")
else:
    print("Không tìm thấy khóa bí mật.")
