
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import binascii
message=b'This message is signed'
signerkey = RSA.import_key(open('privatekey.pem').read())
verifyingkey=RSA.import_key(open('publickey.pem').read())
h=SHA256.new()
h.update(message)
signer = PKCS115_SigScheme(signerkey)
signature = signer.sign(h)
print("Signature:", binascii.hexlify(signature))

msg = b'This message is signed'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(verifyingkey)
try:
    signer.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

msg = b'A tampered message'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(signerkey)
try:
    signer.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")