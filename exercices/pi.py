import random
iteration = int(input("Nombre d'itération"))

def calcul_pi(num):
        total = 0
        for i in range(1,num+1):
            total = total + 1/i**4
        return (total*90)**(1/4)



def calcul_pi2(num):
        cercle = 0
        for i in range (1,num+1):
            x,y = random.random(), random.random()
            if x**2 + y**2 <= 1:
                cercle += 1
        return cercle/num*4

print (calcul_pi(iteration))
print (calcul_pi2(iteration))
