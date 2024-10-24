
from Crypto.Util.number import getPrime, inverse

def encrypt(message, e, n):
    # Mã hóa thông điệp
    return pow(message, e, n)
# Bước 1: Tạo số nguyên tố p, q
p = getPrime(512)  # Số nguyên tố 512 bit
q = getPrime(512)

n = p * q  # Tính n
phi_n = (p - 1) * (q - 1)  # Tính Euler's Totient function

# Bước 2: Chọn e sao cho 1 < e < phi_n và gcd(e, phi_n) = 1
e = 65537  # Giá trị e phổ biến
message = 19051890
# Bước 3: Tính khóa bí mật d
#d = inverse(e, phi_n)
print(f"Public Key (e, n): ({e}, {n})")
encrypted_message = encrypt(message, e, n)
print("Thông điệp đã mã hóa:", encrypted_message)
# Xuất kết quả
#print(f"Private Key d: {d}")
