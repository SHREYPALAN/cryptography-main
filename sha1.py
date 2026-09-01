#write a program to find out message digest (hash value) from sh1 algorithim

import hashlib

text = input ("enter a string  to genrate hash:")

sha1_result = hashlib.sha1(text.encode())
print("\n--- SHA-1 HASH ---")
print("SHA-1 (hex):",sha1_result.hexdigest())
print("SHA-1 output size(in bits):",len(sha1_result.digest())*8)
