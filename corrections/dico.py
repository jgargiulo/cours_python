class KeyException(Exception): pass

def index(dic, value):
    for k,v in dic:
        if v == value:
            return k
    raise KeyException

def is_in(dic, key):
    for k, _ in dic:
        if k == key:
            return True
    return False

def drop(dic, k):
    if not is_in(dic, k):
        raise KeyException

    v = get(dic, k)
    dic.remove( (k,v) )
    return v

def get(dic, karg):
    for k, v in dic:
        if k == karg:
            return v
    raise KeyException

def add(dic, k, v):
    if is_in(dic, k):
        drop(dic, k)

    dic.append( (k,v) )

def get_or_else(dic, karg, default):
    for k, v in dic:
        if k == karg:
            return v
    return default

def get_or_else_v2(dic, karg, default):
    try:
        return get(dic, karg)
    except KeyException:
        return default

def get_or_else_v3(dic, karg, default):
    if not is_in(dic, karg):
        return default
    return get(dic, karg)

def length(dic):
    return len(dic)


def values(dic):
    res = []
    for _, v in dic:
        res.append(v)
    return res

def keys(dic):
    res = []
    for k, _ in dic:
        res.append(k)
    return res

def reverse(dic):
    res = []
    for k,v in dic:
        add(res, v, k)
    return res

if __name__ == "__main__":
    dic = []
    add(dic, "nom", "Cavat")
    add(dic, "prenom", "Joel")
    add(dic, "city", "Geneva")
    add(dic, "city2", "Geneva")
    print(dic)
    print(values(dic))
    print(reverse(dic))




    

