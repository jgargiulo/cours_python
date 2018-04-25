def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
def fibo2(n):
    a = 0
    b = 1
    for i in range(n):
        b = a + b
        a = b - a
    return a
    
