import  hashlib

message = input ("enter text:")
h = hashlib.sha512(message.encode()).hexdigest()
print("Hash value",h)
