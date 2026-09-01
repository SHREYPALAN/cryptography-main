import  hashlib

message = input ("enter text:")
h = hashlib.md5(message.encode()).hexdigest()
print("Hash value",h)
