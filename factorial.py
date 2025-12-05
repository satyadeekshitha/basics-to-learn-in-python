# in factorial we use range fuction to genarate a sequence of numbers
# and in factorial we take a temparary variable as 1 not 0 
fact = 1
for i in range(4,1,-1):
    fact = fact *i
print(f"the facotrial of {fact}")
