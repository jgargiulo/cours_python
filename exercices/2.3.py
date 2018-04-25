
def strict_positif(a):
    return a > 0 

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

    # return a if a > b else b

def minimum(a,b):
    if maximum(a, b) == a:
        return b
    return a

def negatif(a):
    return minimum(a, 0) == a

def negatif2(a):
    return maximum(a, 0) == 0

    
def pair(a):
    return a % 2 == 0

def oppose(a):
    return -a

def absolue(a):
    return oppose(a) if negatif(a) else a

def f(x):
    return maximum(2, x)

def g(x):
    return maximum(-1, minimum( 6, 2*x ) ) 
