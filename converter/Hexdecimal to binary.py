##Hex to bin
HexDecimal = str(raw_input("Enter HexDecimal number ONLY: "))

##this def is used for index the HEX to numbers
def hexindex(hex1):
    numbers = '0123456789'
    if hex1 in numbers:
        return hex1
    else:
        if hex1 == 'a':
            return 10
        elif hex1 == 'b':
            return 11
        elif hex1 == 'c':
            return 12
        elif hex1 == 'd':
            return 13
        elif hex1 == 'e':
            return 14
        elif hex1 == 'f':
            return 15


##this def is used for index the base64 - mapping numbers to char's
##def base64index(b64):
from string import maketrans
def base64index(b64):
    value =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']
    char = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    base64map = value[char.index(b64)]
    return base64map


'''
    intab = 
    outtab = "12345"
    trantab = maketrans(intab, outtab)
'''


binarystr = ''
binarylist = []
##convert the Hex to bin
for lop in range(len(HexDecimal)):
    binary = bin(int(hexindex(HexDecimal[lop])))[2:]
    if binary == '0':
        binary = '0000'
    binarystr += binary
    print binarystr

    ##check the binary and make the string of 24 bit long
    if len(binarystr) == 6:
        bin6long1 = binarystr[0:6]
        bin6long2 = binarystr[6:12]
        bin6long3 = binarystr[12:18]
        bin6long4 = binarystr[18:]
        if len(bin6long4) != 6:
            bin6long4 += (6 - len(bin6long4)) * '0'
        ##Binary (base on 6 bit) convert to to Decimal
        value1 = []
        value2 = []
        value3 = []
        value4 = []
        listbase64 = ''
        for lop in range(6):
            value1.append(int(bin6long1[lop]) * (2 ** ((len(bin6long1) - 1) - lop)))
            value2.append(int(bin6long2[lop]) * (2 ** ((len(bin6long2) - 1) - lop)))
            value3.append(int(bin6long3[lop]) * (2 ** ((len(bin6long3) - 1) - lop)))
            value4.append(int(bin6long4[lop]) * (2 ** ((len(bin6long4) - 1) - lop)))
            value1sum1 = sum(value1)
            value1sum2 = sum(value2)
            value1sum3 = sum(value3)
            value1sum4 = sum(value4)
        print value1sum1
        print value1sum2
        print value1sum3
        print value1sum4
        listbase64 += base64index(value1sum1)+base64index(value1sum2)+base64index(value1sum3)+base64index(value1sum4)
        print listbase64


