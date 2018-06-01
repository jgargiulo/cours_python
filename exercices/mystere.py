import random
#def mystere():
nbreusr = 0
nbre = random.randint(1,2)

while nbreusr != nbre:
    nbreusr = int(input("Choisir un nombre entre 1 et 2 :"))
    if nbreusr != nbre:
        print ("try again")

print ("you found the number", nbreusr)
