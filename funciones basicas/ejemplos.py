def sumar (a, b):
    return a + b
resultado = sumar (3, 5)


def factorial (n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial (n-1)
    
print(factorial(5))