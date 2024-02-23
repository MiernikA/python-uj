# 4.3
def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac


# 4.4
def fibonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c

    return c


# Example usage 
print(factorial(5))
print(fibonacci(6))
