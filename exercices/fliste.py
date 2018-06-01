#retourne la longueur d'une liste


def lsize(liste):
    count = 0
    for i in liste:
        count += 1
    return count

def laverage(liste):
    total = 0
    for i in liste:
        total += i
    return total/lsize(liste)

def plusgrandouegal(liste,seuil):
    result = []
    for i in liste:
        if i >= seuil:
            result.append(i)
    return result

def pluspetitouegal(liste,seuil):
    result = []
    for i in liste:
        if i <= seuil:
            result.append(i)
    return result

def positive(liste):
    result = []
    for i in liste:
        if i >= 0:
            result.append(i)
    return result

def negative(liste):
    result =[]
    for i in liste:
        if i <= 0:
            result.append(i)
    return result

def dans(liste,nbre):
    result = []
    for i in liste:
        if i == nbre:
            return True
    return False

def minimum(liste):
    liste.sort()
    return liste[0]


def maximum(liste):
    liste.sort()
    return liste[-1]

def repeter(liste,repeat):
    result = ""
    while repeat != 0:
        print(liste)
        repeat =repeat-1

def binaire(liste):
    result = 0
    for i,v in enumerate(reversed(liste)):
        result += int(v)*2**i
    return result

def and_lst(liste):
    result = True
    for i in liste:
        result = result and i
    return result

def or_lst(liste):
        result = False
        for i in liste:
            result = result or i
        return result

def table_mult(val):
    for i in range(2, val+1):
        for j in range(2,val+1):
            print(i,j,i*j)
# [], [] -> []
def zip(a,b):
    restuple = []
    #index = 0
    if lsize(a) != lsize(b):
        return restuple

    for i in range (len(a)):
        restuple.append((a[i],b[i]))
        #index += 1
    return restuple

# [(A, B)] -> [A], [B]
def unzip(a):
    lst1 = []
    lst2 = []
    for i,j in a:
        lst1.append(i)
        lst2.append(j)
    print (lst1,lst2)


def tranform(lst, f):
    res= []
    for elem in lst:
            rest.append(f(elem))
    return res

# [A], A->Bool -> [A]
def filter(lst, p):
    res = []
    for elem in lst:
        if p(elem):
            res.append(elem)
    return res

#def pair(x):
#    return x%2==


#def remove_duplicate(lst):

#    for i in lst:

class IndexException(Exception):
    pass

def get(dic,key):
    for k,v in dic:
        if k == key:
            return v

def drop(dic,k):
    v = get(dic,k)
    dic.remove((k,v))
    return v

    #for k,v in dic:
    #    if k == key:
    #        dic.remove((k,v))
    #            return k

def is_in(dic,key):
    for k, _ in dic:
        if k == key:
            return True
    return False


def add(dic,k,v):
    if is_in(dic,v):
        drop(dic,k)
        dic.append((k,v))
    else:
        dic.append((k,v))

def length(dic):
    return len(dic)

def index(dic,val):
    for k,v in dic:
        if val == v:
            return k
    raise IndexException('al not in dic'.format(val))

def values(dic):
    val = []
    for k,v in dic:
        val += v
    return val

def key(dic):
    keys = []
    for k,v in dic:
        keys.append(k)
    return keys

def reverse(dic):
    res = []
    for k,v in dic:
        res.append((v,k))
    return res


    #while (res != True ):
    #    res = k in dic
#    return (res)
