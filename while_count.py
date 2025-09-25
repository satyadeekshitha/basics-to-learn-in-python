n = int(input())
first = 0 
second = 1
next = first + second
count=2
print(first," ",second)
while(count <= n):
    print(next, " ")
    first = second
    second = next
    next = first + second
    count = count + 1
    