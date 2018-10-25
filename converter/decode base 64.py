## this is for decoding base64 format
import base64
from Crypto.Cipher import AES
var1 = str(input('Please type string for decoding in base64: '))
print(base64.b64decode(var1))




