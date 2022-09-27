from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
message='Hello'
salt=get_random_bytes(16)
h = SHA256.new()
h.update(message.encode())
#print (h.hexdigest())

#print(salt)