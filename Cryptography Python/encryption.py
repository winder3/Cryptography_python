from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
#pad is making sure the text is 128 bytes

key=b'thiskeyisbasic12' #16 byte password
cipher=AES.new(key,AES.MODE_CBC)
plaintext=b"This is the message to be encrypted and oh nyo"
ciphertext=cipher.encrypt(pad(plaintext,AES.block_size))
print(cipher.iv)
with open('cipher_file','wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)