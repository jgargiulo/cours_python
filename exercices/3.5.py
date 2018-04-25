
# () -> int
def demande_entier():
    res = input("Entre un nombre entier: ")
    while not res.isnumeric():
        res = input("Entre un nombre entier: ")
    return int(res)

def mystere(n):
    guess = demande_entier()
    while guess != n:
        print("Oups, essayez encore")
        if guess < n:
            print("Le nombre est plus grand")
        else:
            print("Le nombre est plus petit")
        guess = demande_entier()
    print("Bravo, vous avez trouvé")
