def swap(a,b):
    print("A is %d and B is %d", a,b)

    temp = a
    a = b
    b = temp
    print("A is %d and B is %d",a,b)
swap(4,3)

def swap_numbers(x, y):
    print(f"recived :x = {x}, y = {y}")
    x, y = y, x
    print(f"swapped :x = {x}, y = {y}")
    return x,y
num_1  = 9
num_2  = 8
print(swap_numbers(num_1,num_2))   


def swap_list(x,y):
    z = x + y
    x = z - x
    y = z - y
    print("after swapping :",x)
    print("after swapping:", y)    
swap_list(5,6)

   