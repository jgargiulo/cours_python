
# 1.1
# [T] => int 
def longueur(xs):
    res = 0
    for x in xs:
        res += 1
    return res

# 1.2
# [num] => float 
def moyenne(xs):
    somme = 0
    for x in xs:
        somme += x
    l = longueur(xs)
    return somme / l if l > 0 else 0

# 1.3
# [num] => [num]
def plus_grand_ou_egal(xs, n):
    ys = [] 
    for x in xs:
        if x >= n:
            ys.append(x)
    return ys

# 1.4
# [num] => [num]
def plus_petit_ou_egal(xs, n):
    ys = []
    for x in xs:
        if x <= n:
            ys.append(x)
    return ys

# 1.5
# [num] => [num]
def positive(xs):
  return plus_grand_ou_egal(xs, 0)

# 1.6
# [num] => [num]
def negative(xs):
  return plus_petit_ou_egal(xs, 0)

# 1.7
# [T] => bool
def dans(xs, n):
  for x in xs:
    if n == x:
      return True
  return False

# 1.8
# [num] => num
def minimum(xs):
  rep = xs[0]
  for x in xs:
    if x < rep:
      rep = x
  return rep
    
# 1.9
# [num] => num
def maximum(xs):
  rep = xs[0]
  for x in xs:
    if x > rep:
      rep = x
  return rep

# 1.10
# (str, int) => ()
def repeter(texte, n):
  for i in range(n):
    print(texte)

from fractions import Fraction
# 1.11
# (num) => Fraction
def radian(degre):
  return Fraction(degre, 180)

# 1.12
# (num) => num
def degre(radian):
  return (radian * 180) % 360

# 1.13
# [str] => num
def binaire(bits):
  res = 0
  for i, b in enumerate(reversed(bits)):
    res += int(b) * 2 ** i
  return res

# 1.14
# [bool] => bool
def and_lst(xs):
  res = True
  for x in xs:
    res = res and x
  return res

# 1.15
# [bool] => bool
def or_lst(xs):
  res = False 
  for x in xs:
    res = res or x
  return res

# 1.16
# (int) => ()
def table_mult(n):
  for i in range(2, n+1):
    for j in range(2, n+1):
      print(i, " * ", j, " = ", i * j)

# 1.17
# ([num], [num]) => [(num, num)]
def zip(xs, ys):
  zs = []
  if len(xs) != len(ys):
    return zs
  for i in range(len(xs)):
    zs.append((xs[i], ys[i]))
  return zs

# 1.18
# [(num, num)] => ([num], [num])
def unzip(xs):
  (ys, zs) = ([], [])
  for (x1, x2) in xs:
    ys.append(x1)
    zs.append(x2)
  return (ys, zs)

# 1.19
# ([A], A => B) => [B]
def transform(xs, f):
    res = []
    for x in xs:
        res.append(f(x))
    return res

# 1.20
# ([T], T => bool) => [T]
def filter(xs, predicate):
  ys = []
  for x in xs:
    if predicate(x):
      ys.append(x)
  return ys


# ([T], T => bool) => ([T], [T])
def partition(xs, predicate):
  ys, zs = [], []
  for x in xs:
    if predicate(x):
      ys.append(x)
    else:
      zs.append(x)
  return ys, zs

l1 = [-4, -3, -2, 0, 5, 6, 7]
l2 = [-1, 0, 1]
l3 = []

# longueur
assert( longueur(l1) == len(l1) )
assert( longueur(l2) == len(l2) )
assert( longueur(l3) == len(l3) == 0 )

# moyenne(xs):
assert( moyenne(l1) == sum(l1) / len(l1) )
assert( moyenne(l2) == sum(l2) / len(l2) )
assert( moyenne(l3) == 0.0 )

# plus_grand_ou_egal(xs, n):
assert( plus_grand_ou_egal(l1, 0) == [0, 5, 6, 7] )
assert( plus_grand_ou_egal(l2, 1) == [1] )
assert( plus_grand_ou_egal(l3, 4) == l3 )

# plus_petit_ou_egal(xs, n):
assert( plus_petit_ou_egal(l1, 3) == l1[0:4] )
assert( plus_petit_ou_egal(l2, 0) == [-1, 0] )
assert( plus_petit_ou_egal(l3, 4) == l3 )

# positive(xs):
assert( positive(l1) == filter(l1, lambda x: x >= 0) )
assert( positive(l2) == filter(l2, lambda x: x >= 0) )
assert( positive(l3) == filter(l3, lambda x: x >= 0) )

# negative(xs):
assert( negative(l1) == filter(l1, lambda x: x <= 0) )
assert( negative(l2) == filter(l2, lambda x: x <= 0) )
assert( negative(l3) == filter(l3, lambda x: x <= 0) )

# dans(xs, n):
for i in range(-10, 11):
  assert( dans(l1, i) == (i in l1) )
  assert( dans(l2, i) == (i in l2) )
  assert( dans(l3, i) == (i in l3) )

# minimum(xs):
assert( minimum(l1) == min(l1) )
assert( minimum(l2) == min(l2) )
	
# maximum(xs):
assert( maximum(l1) == max(l1) )
assert( maximum(l2) == max(l2) )

# repeter(texte, n):
repeter("Bonjour", 3)
repeter("Nooon", 0)
repeter("Nooon", -10)

# radian(degre):
assert( radian(180) == 1 )
assert( radian(72) == Fraction(2,5) )
assert( radian(60) == Fraction(1, 3) )
assert( radian(45) == Fraction(1, 4) )
assert( radian(30) == Fraction(1, 6) )
assert( radian(240) == Fraction(4, 3) )
print( radian(2000) )

# degre(radian):
assert( degre(1/4) == 45.0 )
assert( degre(1/6) == 30.0 )
assert( degre(Fraction(5,12)) == 75 )

# binaire(bits):
assert( binaire("0101") == 5 )
assert( binaire("1010") == 10 )
assert( binaire("10101") == 21 )

# and_lst(xs):
assert( and_lst([True, True, False]) == False )
assert( and_lst([True, True]) == True )

# or_lst(xs):
assert( or_lst([True, True, False]) == True )
assert( or_lst([True, True]) == True )
assert( or_lst([False, False, False]) == False )

# table_mult(n):
table_mult(4)

# zip(xs, ys):
assert( zip([1, 2, 3], "abc") == [(1, "a"), (2, "b"), (3, "c")] )

# unzip(xs):
assert( unzip(zip([1, 2, 3], "abc")) == ([1,2,3], ["a", "b", "c"]) )

# transform(xs, f):
assert( transform(l1, lambda x: 2*x+3) == list(map(lambda x: 2*x+3, l1)) ) 

# filter(xs, predicate):
assert( filter(l1, lambda x: x >= 0) == positive(l1)  ) 











