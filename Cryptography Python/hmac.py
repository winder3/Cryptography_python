from Crypto.Hash import HMAC, SHA256
import random
key = b'Swordfish'
msg='Oh nyo its exposed'
#mac=random.choice(['81ac211952fab5a807d021e5dec34203ce4ec771804a7eefbed4de1ddd60f6e0','81ac211952fab5a807d021e5dec34203ce4ec771804a7eefbed4de1ddd60f6e1'])
h = HMAC.new(key, digestmod=SHA256)
h.update(msg.encode())
#mac=h.hexdigest()
try:
  h.hexverify(mac)
  print("The message '%s' is authentic" % msg)
except ValueError:
  print("The message or the key is wrong")
