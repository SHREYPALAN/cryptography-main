#write a program to find out message digest (hash value) from sha512 algorithim

import hashlib

text = input ("enter a string  to genrate hash:")

sha512_result = hashlib.sha512(text.encode())
print("\n--- SHA-1 HASH ---")
print("SHA-512 (hex):",sha512_result.hexdigest())
print("SHA-512 output size(in bits):",len(sha512_result.digest())*8)
