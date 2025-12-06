# in factorial we use range fuction to genarate a sequence of numbers
# and in factorial we take a temparary variable as 1 not 0 
fact = 1
for i in range(6,1,-1):
    fact = fact *i
print(f"the facotrial of {fact}")
# 6,5,4,3,2
"""
1 = 1*6 = 6
2 = 6*5 = 30
3 = 30*4 = 120
4 = 120*3 = 360
5 = 360*2 = 720
"""



