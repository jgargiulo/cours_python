

first, last = 0 ,1
iteration = int(input("Choisir le nombre d'itération"))

for i in range(1,iteration):
    last, first = first + last, last


print (first)
