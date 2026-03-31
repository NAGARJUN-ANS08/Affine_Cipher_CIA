import struct
message = "HELLO" 
message_size = 5
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


def rotation(x,n):
    return ((x << n) | (x >> (64 - n))) & 0xffffffffffffffff

def sipround(h1,h2,h3,h4):
    h1 += h2
    h2 = rotation(h2,7)
    h2 ^= h1
    h1 = rotation(h1,17)

    h3 += h4
    h4 = rotation(h4,7)
    h4 ^= h3

    h1 += h4
    h4 = rotation(h4,7)
    h4 ^= h1

    h3 += h2
    h2 = rotation(h2,7)
    h2 ^= h3
    h3 = rotation(h3,17)

    return h1,h2,h3,h4

def siphash(key1,key2,message):
    h1 = key1 ^ 0x736f6d6570736575
    h2 = key2 ^ 0x646f72616e646f6d
    h3 = key1 ^ 0x6c7967656e657261
    h4 = key2 ^ 0x7465646279746573

    for c in message:
        m = ord(c)
        h4 ^= m

        for _ in range(2):
            h1,h2,h3,h4 = sipround(h1,h2,h3,h4)

        h1 ^= m

    h3 ^= 0xff

    for _ in range(4):
        h1,h2,h3,h4 = sipround(h1,h2,h3,h4)

    return h1 ^ h2 ^ h3 ^ h4

key1 = 0x12345678
key2 = 0x9abcdef0

Hash_Value = siphash(key1,key2,message)
print("Hash Output : ",Hash_Value)

concatenate_msg = str(Hash_Value) + message

Encrypted_cipher = affine_encrypt(concatenate_msg,a,b)
print("Encrypted output : ",Encrypted_cipher)

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

def auth(Decrypt,key1,key2,message_size):
     New_Hash = Decrypt[:-message_size]
     New_msg = Decrypt[-message_size:]
     Auth_hash = siphash(key1,key2,New_msg)
     if(Auth_hash == int(New_Hash)):
         print("Authentication Successful") 
     else:
         print("Authentication Unsuccessful")
        
auth(Decrypt,key1,key2,message_size)