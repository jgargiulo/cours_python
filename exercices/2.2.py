

# num -> num
def f(x): 
    return 3*x + 2

# num -> num
def g(x): return x**2


# (num, num) -> num
def h(x, y): 
    return x + 2*y

# num -> str
def i(x): 
    return str(x)

# num -> num
def j(x):
    return f(g(x))

# (num, num) -> str
def k(x, y):
    return i( h(x, y) ) 

a = float(input("Entrez une valeur: "))
b = float(input("Entrez une deuxième valeur: "))
x = input("Entrez une fonction: ")

print( eval( x ) (a,b) )




