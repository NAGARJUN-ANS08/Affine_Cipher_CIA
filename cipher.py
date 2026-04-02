import struct
message = input("Enter plain text: ")

message_size = len(message)
a = 5
b = 8

def char_to_num(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    elif '0' <= c <= '9':
        return ord(c) - ord('0') + 52
    else:
        return None
    
def num_to_char(n):
    if 0 <= n < 26:
        return chr(n + ord('A'))
    elif 26 <= n < 52:
        return chr(n - 26 + ord('a'))
    elif 52 <= n < 62:
        return chr(n - 52 + ord('0'))
    
def affine_encrypt(con_text,a,b):
    res = ""
    for char in con_text:
        x = char_to_num(char)
        if x is not None:
            enc = (a * x + b) % 62
            res += num_to_char(enc)
        else:
            res += char
    return res
Encrypted_cipher = affine_encrypt(message,a,b)
print("Encrypted value : ", Encrypted_cipher)

m = 62
a_inv = pow(a, -1, m)

def affine_decrypt(Encrypted_cipher,a_inv,b):
    res2 = ""

    for char in Encrypted_cipher:
        y = char_to_num(char)

        if y is not None:
            dec = (a_inv * ((y - b) % 62)) % 62
            res2 += num_to_char(dec)
        else:
            res2 += char

    return res2

Decrypt = affine_decrypt(Encrypted_cipher,a_inv,b)

print("Decrypted_value : ", Decrypt)