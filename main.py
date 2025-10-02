import inspect
# Exemple avec un seul exercice
def exercise1():
    print("Bonjour tout le monde !")


def exercise2(use=False):
    name = input("Quel est votre prénom ? ")
    if not use :
        print("Boujour", name, "!")
    return name


def exercise3():
    print("Première ligne\nDeuxième ligne\nTroisième ligne")


def exercise4(use=False):
    year_birth = int(input("Année de naissance ? "))
    if not use :
        print("Vous avez environ : ", 2025-year_birth, "ans")
    return 2025-year_birth


def exercise5():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    print(f"{n1} + {n2} = ", n1+n2)


def exercise6():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    print(f"{n1} - {n2} = ", n1 - n2)


def exercise7():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    print(f"{n1} * {n2} = ", n1 * n2)


def exercise8():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    if n2 == 0:
        print("On ne peut pas diviser par zéro")
    else:
        print(f"{n1} / {n2} =", n1 / n2, "et", f"{n2} / {n1} =", n2 / n1)


def exercise9():
    n = int(input("Tapez un nombre : "))
    print(f"Le carré de {n} est :", n*n)


def exercise10():
    n = int(input("Tapez un nombre : "))
    print(f"Le double de {n} est :", n*2)


def exercise11():
    n = int(input("Tapez un nombre : "))
    print(f"la moitié de {n} est :", n**2)


def exercise12():
    for i in range(5):
        print("Le message apparaît 5 fois.")


def exercise13():
    for i in range(5):
        print(i + 1)


def exercise14():
    for i in range(5):
        print(f"{2} x {i + 1} = {2 * (i+1)}")


def exercise15():
    length = int(input("Tapez la dimension du côté du carré : "))
    print(f"Périmètre du carré : {length*4}")


def exercise16():
    length = int(input("Tapez la dimension du côté du carré : "))
    print(f"Aire du carré : {length*length}")


def exercise17():
    nb_euro = int(input("Nombre d'euro ? "))
    print(f"{nb_euro} € = {nb_euro*1.1} $")


def exercise18():
    minutes = int(input("Entrez les minutes : "))
    print(f"{minutes} minutes = ", minutes*60, "secondes")


def exercise19():
    price_HT = int(input("Entrez le prixe HT : "))
    print(f"Prix TTC =", price_HT + price_HT/5, "€")


def exercise20(name,year):
    print(name, "a", year, "ans")


def exercise21():
    n = int(input("Tapez un nombre : "))
    if n>5:
        print(n, "-> Positif")
    elif n<5:
        print(n, "-> Négative")
    else:
        print(n, "-> Nul")


def exercise22():
    year = int(input("Tapez votre âge : "))
    if year<18:
        print("Vous êtes mineur")
    else:
        print("Vous êtes majeur")


def exercise23():
    n = int(input("Tapez votre note : "))
    if n < 10:
        print(n, "-> Non validé")
    else:
        print(n, "-> Validé")


def exercise24():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    if n1>n2 :
        print(n1, "est le plus grand")
    elif n1<n2 :
        print(n2, "est le plus grand")
    else:
        print("Les deux nombres sont égaux")


def exercise25():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    if n1 > n2:
        print(n1, "et", n2, "-> ordre décroissant")
    elif n1 < n2:
        print(n1, "et", n2, "-> ordre croissant")
    else:
        print("Les deux nombres sont égaux")


def exercise26():
    n = int(input("Tapez un nombre : "))
    if n%5 == 0:
        print("Divisible par 5")
    else:
        print("Pas divisible par 5")


def exercise27():
    year = int(input("Tapez votre âge : "))
    if year < 12:
        print("Vous êtes un enfant")
    elif 12 <= year <= 17:
        print("Vous êtes un adolescent")
    else:
        print("Vous êtes un adulte")



def main(exercise_list):
    choice = int(input("Entrez le numéro de l'exercice à exécuter : "))
    for i in range(0, len(exercise_list)):
        if choice == i + 1:
            print("\nExercise", choice, ":\n")
            if choice == 21:
                use = True
                exercise_list[i](exercise_list[1](use), exercise_list[3](use))
                break
            exercise_list[i]()
            break



if __name__ == "__main__":
    main(exercise_list = [obj for name, obj in globals().items() if inspect.isfunction(obj)][:-1])

