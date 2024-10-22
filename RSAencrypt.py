def encrypt(message, e, n):
    # Mã hóa thông điệp
    return pow(message, e, n)

if __name__ == "__main__":
    # Nhập khóa công khai e và n
    e = 17993
    n = 90581

    # Nhập thông điệp bản rõ
    message = 011100000111010001101001011101000101111101110111011010010110010101101110011001010111001001011111011000010111010001110100011000010110001101101011

    # Mã hóa thông điệp
    encrypted_message = encrypt(message, e, n)
    print("Thông điệp đã mã hóa:", encrypted_message)