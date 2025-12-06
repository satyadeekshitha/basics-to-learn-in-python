# fibonacci series is the series of numbers where each number is the sum of the two preceding numbers
# the fibonacci series starts with 0 and 1
n = int(input())
first = 0
second = 1
next = first + second
count = 2
while(count < n):
    first = second
    second = next
    next = first + second
    count = count + 1
print(second)
# for the nth term in the fibonacci series
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())

result = fibonacci(n)

print(result)

    
    