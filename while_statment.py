t = int(input())
num  = t
rev = 0
while(t!= 0):
    a = t%10
    rev = (rev*10)+ a
    t = (int)(t/10)
print("reverse order is ",str(rev)) 

if (rev== num):
    print("my input is palindrome")
else:
    print("it is not a palindrome")    
