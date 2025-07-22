#Using Loop

def factorial_loop(n):
    result = 1

    for i in range(1, n+1):
        result*= i
    return result

result= factorial_loop(5)
    
print(result)


