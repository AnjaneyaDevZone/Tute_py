def factorial(n):

    #To calculate the factorial of a number
    if n <2:
        return 1
    else:
        return n * (factorial(n-1))
result = factorial(5)
print(result)

