##Hex to bin and bin to base64
import binascii
import base64
HexDecimal = str(raw_input("Enter HexDecimal number ONLY: "))
var1 = binascii.a2b_hex(HexDecimal)
print var1
print base64.b64encode(var1)

