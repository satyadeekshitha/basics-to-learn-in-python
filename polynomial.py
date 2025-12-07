x = 2
P_x = 3 * (x**3) + 2 * (x**2) - 5 * x + 7
print(P_x) 

def naive_eval(coeffs, x):
    result = 0
    for i in range(len(coeffs)):
        result += coeffs[i] *  (x ** i)
    return result
coeffs = [7, -5, 2, 3] # here range is used to give value of i like x^0
#here in coeffs highest power is at the end 
print(naive_eval(coeffs, 2) ) #

# to reverse the order of coeffs lengths:
coeffs = [7, -5, 2, 3]
forward_coeffs = list(range(len(coeffs)))
reversed_coeffs = forward_coeffs[::-1]
print(reversed_coeffs)


# do the same thing again

#HORNER'S METHOD
def horner_eval(coeffs, x):
    result = 0
    for coef in reversed(coeffs):
        result = coef + x * result
    return result
coeffs = [3, 2, -5, 7] # 3x*3 + 2x*2 - 5x + 7
print(horner_eval(coeffs, 2))

def naive_eval(coeffs, x):
    result = 0
    for i in range(len(coeffs)):
        result += coeffs[i] *(x**i)
    return result
# there is polyval() function in numpy to evaluate polynomial


