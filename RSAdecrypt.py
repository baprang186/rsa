from Crypto.Util.number import long_to_bytes

def decrypt_rsa(ciphertext, d, n):
    # Giải mã bản mã
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Ví dụ sử dụng
ciphertext = 61755  # Bản mã (dạng số nguyên)
d = 5  # Khóa bí mật
n = 90581  # Modulus

# Giải mã
plaintext = decrypt_rsa(ciphertext, d, n)
print("Bản rõ:", plaintext)