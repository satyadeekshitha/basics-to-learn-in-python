a = 1234
bin(a) #binary representation of a
print((bin(a))) # '0b11010010'
oct(a) # octal representation of a
print(oct(a)) #'0o2322'
hex(a) # hexadecimal representation of a
print(hex(a)) #'0x4d2'
int(0b11) # binary to decimal
print(int(0b11)) # 3
int(0o11) # octal to decimal    
print(int(0o11)) # 9
int(0x11) # hexadecimal to decimal
print(int(0x11)) # 17
# convert from decmial to binary
def dec_to_bin(a):
    b = 0
    while(a != 0):
        remainder = a%2
        b = b*10 + remainder
        a = int(a/2)
    return b    
a = dec_to_bin(16)
print(a) # 10000        




