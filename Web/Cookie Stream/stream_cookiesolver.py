from binascii import hexlify, unhexlify
from Crypto.Util.Padding import pad, unpad

orig_auth = '895462eacc651da4dd302f43d42eaccaffab31053df1cb60'

nonce = '895462eacc651da4' #First 16Bytes
ciphertext1 = "dd302f43d42eaccaffab31053df1cb60" #Last 32Bytes
plaintext1 = "Eth007"
plaintext2 = "admin"

#As plaintext1 XOR plaintext2 = Ciphertext1 XOR X

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

plaintext1 = (pad(plaintext1.encode(),16))
plaintext2 = (pad(plaintext2.encode(),16))

p1XORp2 = byte_xor(plaintext1, plaintext2)

ciphertext1 = unhexlify(ciphertext1)

c1XOR_p1XORp2_ = byte_xor(ciphertext1, p1XORp2)

print(" New Auth-Cookie: " + nonce + hexlify(c1XOR_p1XORp2_).decode())

### New Auth-Cookie: 895462eacc651da4f9202a1a8a12adcbfeaa30043cf0ca61