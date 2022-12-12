from math import gcd as bltin_gcd
from Crypto.Util.number import inverse
import binascii

message = input("Enter the message to be encrypted: ")
print(f"original text: [{message}]")

m = ""
for x in message:
    m += str(ord(x))
m = int(m)
print(f"m: [{m}]")

#step 1 choose 2 primes
p = 338188833166782510389682911521
q = 179656495802618509563276524693
print(f"p: [{p}]\nq: [{q}]\n")

#step 2 get n
n = p * q
print(f"n: [{n}]\n")
#step 3 get phi
phi = (p - 1) * (q - 1)
print(f"phi: [{phi}]\n")

#step 4 choose e -- must be 1 < e < phi(n) && coprimes with n and phi
e = 65537
for num in range(2, phi):
    if (bltin_gcd(num, n) == 1) and (bltin_gcd(num, phi) == 1):
        e = num
        break
print(f"e: [{e}]")

#step 5 encrypt
c = pow(m,e,n)
print(f"encrypted text: [{c}]\n\n")

print("---------DECRYPTION-----------\n")
#step 6 find d -- d * e mod phi = 1
d = inverse(e, phi)
print(f"d: [{d}]\n")

#step 7 decrypt
decrypted = pow(c, d, n)

print(f"decrypted text: [{decrypted}]")

