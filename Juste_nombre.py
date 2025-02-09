import random
print("Jeu du juste nombre (1 à 1000)")
nombre = random.randrange(0,1001)
réponse = None
essais_restants = int(input("nombre d'essais : "))
while réponse != nombre and essais_restants != 0:
    réponse = int(input("Nombre -> "))
    if réponse > nombre:
        print("Le bon chiffre est plus petit")
    if réponse < nombre:
        print("Le bon chiffre est plus grand")
    essais_restants -= 1
    print("il vous reste", essais_restants, "essais")
print(nombre)