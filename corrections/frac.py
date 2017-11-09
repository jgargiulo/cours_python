def euclide(a,b):
    a, b = abs(a), abs(b)
    if b >= a:
        a,b = b,a
    if b == 0:
        return 0
    r = a % b
    while r is not 0:
        a,b = b,r
        r = a % b
    return b

# prend en paramètre une fraction et retourne
# sa version irréductible
# signature: Tuple -> (int, int)
def reduce(fraction):
    num, den = fraction
    d = euclide(num, den)
    if d is 0:
        return (0, 1)
    return (num // d, den // d)

# Créer une nouvelle fraction irréductible
# ex: fraction(10, 6) retourne (5,3)
# signature: (int, int) -> (int, int)
def fraction(a,b):
    return reduce( (a,b) )
  
# additionne deux fractions  
def add(fr1, fr2):
    a,b = fr1
    c,d = fr2
    return fraction( a*d + b*c, b*d )

  
# soustraction de deux fractions  
def sub(fr1, fr2):
    c,d = fr2
    return add(fr1, (-c, d))
  
# multiplication de deux fractions  
def mul(fr1, fr2):
    a,b = fr1
    c,d = fr2
    return fraction( a*c, b*d )
  
# division de deux fractions  
def div(fr1, fr2):
    c,d = fr2
    return mul(fr1, (d,c) )
