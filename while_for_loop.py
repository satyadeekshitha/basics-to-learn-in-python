# Example: for loop with range
n = 10
for i in range(n):
    c = 0
    c = c + i
    print("c:", c)

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

def iter_example():
    result = 0
    c = 0
    n = 10
    while(c<n):
        result = result + c
        c = c+1
    print("the sum is", result)
    





