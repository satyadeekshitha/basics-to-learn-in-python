t = int(input())
num = t
sum = 0

while(t!=0):
  a = t % 10
  sum = sum + a
  t = int (t /10)
  print(f"the sum is {sum}") # input 123 output 6

# reverse the number:
t = int(input())
num = t
rev = 0
while(t!= 0):
  a = t % 10
  rev=rev*10+a
  t = (int)(t // 10)
  print(f"the reverse of the num is",rev)
if(rev == num):
  print("the number is palindrome")
else:
  print("the number is not palindrome") # input 121 output palindrome and 123 output not palindrome
    