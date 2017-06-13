from string import maketrans
intab = [A, B, C, D, E, F, G, H, I, J]
outtab = [1,2,3,4,5,6,7,8,9 ]
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print str.translate(trantab)