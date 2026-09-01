import  hashlib

message = input ("enter text:")
h = hashlib.sha1(message.encode()).hexdigest()
print("Hash value",h)
