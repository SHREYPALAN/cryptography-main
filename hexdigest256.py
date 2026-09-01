import  hashlib

message = input ("enter text:")
h = hashlib.sha256(message.encode()).hexdigest()
print("Hash value",h)
