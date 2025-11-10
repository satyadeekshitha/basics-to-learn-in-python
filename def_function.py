# def keyword is used to define a function in python
# A function is a block of reusable code that is used to perform a single, related action.
# parameter: variable that is listed within the parentheses of a method header
# argument:a value to assign to the method parameter when it is called
# return is used to evaluate the function and return a value and it stops the function execution
# ex:

def alpha(a,b):
    i = a + b
    return i

alpha = alpha(3,4)
print("alpha",alpha)

# here 3 and 4 are arguments and a and b are parameters

def beta(c,d):
    j = c - d
    return j
x =input()
y =input()
x = int()
y = int()
beta = beta(x,y)
print("beta:", beta)

def alas(a,b):
    k = a+b
    l = a-b
    m = a*b
    return k,l,m
    
x = int(input())    
y = int(input())
k,l,m = alas(x,y)
print(k)
print(l)
print(m)




