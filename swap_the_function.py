# swapping method 1:
def alpha(a,b):
    temp = a
    a = b
    b = temp
    return (a,b)
beta = alpha(64,46)

# swapping method 2 tupple unpacking method:
def swap(a,b):
    a,b = b,a
    return (a,b) 
a = 45
b = 54
print("before swapping a and b:", a,b)
after_swapping = swap(a,b)
print("after swapping a and b:", after_swapping) # prints (54, 45)

# swapping method 3: using arithmetic operations
def swap(x,y):
    x = x+y
    y = x-y
    x = x-y
    return(x,y)
x = 56
y = 87
print("before swapping:",x,y)
after = swap(x,y)
print("after swapping:",after) # prints (87, 56)

