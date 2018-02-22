import string
protasi=raw_input('Give a sentence:')
rot13=string.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
allagi=string.translate(protasi, rot13)
print allagi
