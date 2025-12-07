# Demonstrate how to use range() and convert it to a list
print(list(range(0, 10)))   

n = 10
print(list(range(0, n)))     

print(list(range(n)))        

print(list(range(n, 0, -1))) 

""" 
To find the ASCII= Amirican Standrard code for information interchange value of characters we use ord() function
for example:
"""
print(ord('a')) # prints 97
print(ord('A')) # prints 65
print(ord('z')) # prints 122    
print(ord('0')) # prints 48
print(ord('#')) # prints 35

# to convert ascii character into actual integer value we use chr() function
print(chr(97))  # prints 'a'
print(chr(65))  # prints 'A'    
# method 2
text = "A1B2C3"
numbers = [ord(c) - ord('0') for c in text if '0' <= c <= '9']
print(numbers)  # prints [1, 2, 3]  








