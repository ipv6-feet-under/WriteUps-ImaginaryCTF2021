from binascii import hexlify, unhexlify
from Crypto.Util.Padding import pad, unpad
from bitstring import BitArray

c1 = unhexlify('44940e8301e14fb33ba0da63cd5d2739ad079d571d9f5b987a1c3db2b60c92')
c2 = unhexlify('d208851a855f817d9b3744bd03fdacae61a70c9b953fca57f78e9d2379814c')
flag = unhexlify('696374667b0000000000000000000000000000000000000000000000000000')

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def andbytes(abytes, bbytes):
    return bytes([a & b for a, b in zip(abytes[::-1], bbytes[::-1])][::-1])

def byte_not(a):
    a = str(a)[2:-1]
    a = a.replace('\\x', '')
    c = BitArray(hex=a)
    c = c.bin
    c = c.replace('0','a')
    c = c.replace('1','0')
    c = c.replace('a','1')
    #c = str(c)
    c = int(c,2)
    c = unhexlify('%x' % c)
    return c


#wrong = not (flag XOR c1 XOR c2)

wrong = ''
wrong = byte_xor(flag, c1)
wrong = byte_xor(wrong, c2)
wrong = byte_not(wrong)


print(wrong)