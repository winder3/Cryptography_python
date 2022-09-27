from hashlib import sha256
from Crypto.Hash import SHA256
message='Hello'
h = SHA256.new()
h.update(message.encode())
print (h.hexdigest())
#using encode to derive the message
test=SHA256.new()
test.update(b'Hello')
print(test.digest())
print(test.hexdigest())
#comparing hexadecimal to binary
