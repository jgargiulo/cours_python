def est_numerique(s):
    if s[0] == "-":
        return s[1:].isnumeric()
    return s.isnumeric()

#print(est_numerique('-3'))



def double(xs):
    new = []
    for x in xs:
        if est_numerique(x):
            new.append(int(x)*2)
    return new


def verifier(xs):
    return len(xs) == len(double(xs))
