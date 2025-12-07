# There are two types of data types: primitive and non-primitive data types.
# Primitive data types include:
# int:
a = 10
print("a:", a) # prints 10
# float:
b = 3.4
print("b:", b) # prints 3.4
# string:
c = "Hello Satya" 
print("c:", c) # prints Hello Satya
# boolean:
d = 5
e = 6
if d < e:
    print("d is less than e:", True) # prints True
else:
    print("d is greater than e:", False) # prints False
# Non-primitive data types include:
# list:
# list is mutable(can  be changed)
na_list = [25,10,11,20,7,"the"]
print("na_list:", na_list) # prints [25, 10, 11, 20, 7, 'the']
# tuple:
my_tuple = (25,10,11,200,7)
print("my_tuple:", my_tuple) # prints (25, 10, 11, 200, 7)
# dictionary:
my_dic = {"name": "Satya", "age": 18, "state": "andhra pradesh"}
print("my_dic:", my_dic) # prints {'name': 'Satya', 'age': 18, 'state': 'andhra pradesh'}
# set:
my_set = {25,10,11,200,7}
print("my_set:", my_set) # prints {25, 10, 11, 200, 7}
# here in any type of non primitive data types the index starts from 0
# string are not mutable(can not be changed)
# the several cases of list and string are same like indexing etc but they are differnt
"""
slicing: entering the portion of list 
its like [x:y] here x is starting index and y is ending index but y-1 is the last index which is included
t[-1] means last element 
"""
x = [ 12,34,56,78,90]
"""
here x[-1] we get 90
x[-3,-1] we get 56,78 bcs from last 56 is in 3rd place and in 2nd place 78
"""
"""
* APPEND FUNCTION:
it is used to add an element at the end of the list
* SORT FUNCTION:
it is used change its order either ascending or descending
"""





