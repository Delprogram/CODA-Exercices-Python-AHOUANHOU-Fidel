import inspect
import random


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
        print("Vous avez environ :", 2025-year_birth, "ans")
    return 2025-year_birth


def exercise5():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    print(f"{n1} + {n2} =", n1+n2)


def exercise6():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    print(f"{n1} - {n2} =", n1 - n2)


def exercise7():
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    print(f"{n1} * {n2} =", n1 * n2)


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
    print(f"la moitié de {n} est :", n/2)


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
    elif year <= 17:
        print("Vous êtes un adolescent")
    else:
        print("Vous êtes un adulte")


def exercise28():
    temperature = int(input("Tapez la température de l'eau : "))
    if temperature < 0:
        print("Glace")
    elif temperature <= 100:
        print("Eau liquide")
    else:
        print("Vapeur")


def exercise29():
    note = int(input("Tapez la note : "))
    if note <= 8:
        print("Recalé")
    elif note <= 11:
        print("Passable")
    elif note <= 13:
        print("Assez bien")
    elif note <= 15:
        print("Bien")
    elif note <= 17:
        print("Trés bien")
    else:
        print("Excellent")


def exercise30():
    n = int(input("Tapez un nombre : "))
    for i in range(n):
        print(i + 1)


def exercise31():
    n = int(input("Tapez un nombre : "))
    for i in range(n + 1):
        print(n - i)


def exercise32():
    n = int(input("Tapez un nombre : "))
    som_n = 0
    for i in range(n + 1):
        som_n += i
    print("Somme jusqu'à N =", som_n)


def exercise33():
    n = int(input("Tapez un nombre : "))
    for i in range(10):
        print(f"{n} x {i + 1} = {n * (i+1)}")


def exercise34():
    print("Les nombres :")
    for i in range(11):
        if i % 2 == 0:
            print(i)
    print("sont tous pairs")


def exercise35():
    n = int(input("Tapez un nombre : "))
    print("Les nombres :")
    for i in range(1, n + 1):
        for j in range(1, n - 1):
            if i / j == j:
                print(i)
    print("sont tous des carrés parfaits")


def exercise36():
    word = input("Tapez un mot : ")
    n = int(input("Entrez le nombre de fois qu'on l'affiche : "))
    for i in range(n):
        print(word, end=" ")
    print("\n")


def exercise37():
    print("PYRAMIDE : ")

    print("""       *
   *       *
*    *   *    *""")


def exercise38():
    print("""1 - opération '+'
2 - opération '-'
3 - opération 'x'
4 - opération '/'""")
    operator = input("\nEntrez un des chiffres listés pour choisir l'opération : ")
    n1 = int(input("Tapez un nombre : "))
    n2 = int(input("Tapez un autre nombre : "))
    match operator:
        case "1":
            print(f"{n1} + {n2} = {n1 * n2}")
        case "2":
            print(f"{n1} - {n2} = {n1 * n2}")
        case "3":
            print(f"{n1} * {n2} = {n1 * n2}")
        case "4":
            print(f"{n1} / {n2} = {n1 / n2}")


def exercise39():
    nb_secret = random.randint(1, 100)
    devine = input("Le nombre secret est pair ou impair : ").lower().strip()
    print(nb_secret)
    match devine:
        case "pair":
            if nb_secret % 2 == 0:
                print("GAGNE")
            else:
                print("PERDU")
        case "impair":
            if nb_secret % 2 == 0:
                print("PERDU")
            else:
                print("GAGNE")


def exercise40():
    password = input("Entrez votre mot de passe : ")
    if len(password) < 6:
        print("Trop court")
    else:
        print("Valide")


def exercise41():
    nb_note = int(input("Tapez le nombre de note: "))
    average = []
    average.append(int(input("Entrez votre 1 ère note : ")))
    for i in range(2, nb_note + 1):
        average.append(int(input(f"Entrez votre {i} ème note : ")))
    print(average)
    print("Moyenne =", sum(average)/len(average))


def exercise42():
    n_nbre = int(input("Combien de nombres voulez-vous entrer : "))
    list_nb = []
    min_list = 0
    max_list = 0
    list_nb.append(int(input("Entrez votre 1 er nombre : ")))
    for i in range(2, n_nbre + 1):
        list_nb.append(int(input(f"Entrez votre {i} ème nombre : ")))
    for j, nb in enumerate(list_nb):
        #print(list_nb[j + 1])
        if j == len(list_nb) - 1:
            break
        elif nb <= list_nb[j + 1]:
            min_list = nb
            max_list = list_nb[j + 1]
        else:
            #print("sdvs")
            min_list = list_nb[j + 1]
            max_list = nb
    print("Minimum =", min_list)
    print("Maximum =", max_list)

def exercise43():
    vowels = "aeiou"
    word = input("Tapez un mot : ")
    vowel_word = [x for x in word if x in vowels]
    print(f"Le nombre de voyelles dans {word} est:", len(vowel_word))


def exercise44():
    word = input("Tapez un mot : ")
    reverse_word = [word[-i] for i in range(1, len(word) + 1)]
    print(f"L'inverse de {word} est : {"".join(reverse_word)}")


def exercise45():
    list = [4, 5, 8, 6, 7, 10]
    somme = 0
    for n in list:
        somme += n
    print("Somme =", somme)


def exercise46():
    n = int(input("Tapez un nombre : "))
    list = [4, 5, 8, 6, 7, 10]
    find = False
    if n in list:
        find = True
    if find:
        print(f"{n} est dans la liste")
    else:
        print(f"{n} n'est pas dans la liste")


def exercise47():
    n = int(input("Tapez un nombre : "))
    list = [4, 5, 8, 6, 7, 10, 5, 5]
    find = 0
    for i in list:
        if n == i:
            find += 1
    if find == 0:
        print(f"{n} n'est pas dans la liste")
    else:
        print(f"{n} a été trouvé {find} fois dans la liste")


def exercise48():
    n = int(input("Tapez un nombre : "))
    divisor = []
    divisor = [str(x) for x in range(1, n + 1) if n%x == 0]
    print(f"Les diviseurs de {n} sont :", ", ".join(divisor))


def exercise49():
    n = int(input("Tapez un nombre : "))
    prime_nb = True
    for i in range(2, n):
        if n % i == 0:
            prime_nb = False
            print(f"{n} n'est pas un nombre premier")
            break
    if prime_nb:
        print(f"{n} est un nombre premier")


def exercise50():
    n = int(input("Tapez un nombre : "))
    a = 0
    b = 1
    print("Suite de Fibonacci jusqu'à n = ", n)
    for i in range(0, n):
        print(a)
        a, b = b, a + b


def exercise51():
    n = int(input("Tapez un nombre : "))
    a = 0
    b = 0
    list = [1]
    print(list)
    list2 = [1, 1]
    print(list2)
    for i in range(1, n):
        list2 = [list2[i - 1] + list2[i] for x in range(0, i)]
        list += list2
        print(list)
        #print(list2)









def main(exercise_list):
    while True:
        print("\n=== Menu des exercices ===")
        print("Appuyez sur la touche 'Q' pour QUITTER")
        try:
            choice_str = input("Entrez le numéro de l'exercice à exécuter : ").strip().lower()
            if choice_str == "q":
                print("Au revoir 👋")
                break
            choice = int(choice_str)
            for i in range(0, len(exercise_list)):
                if choice == i + 1:
                    print("\nExercice", choice, ":\n")
                    if choice == 20:
                        use = True
                        exercise_list[i](exercise_list[1](use), exercise_list[3](use))
                        break
                    exercise_list[i]()
                    break
        except:
            print("⚠️ Choix non reconnu. Essayez encore.")





if __name__ == "__main__":
    main(exercise_list = [obj for name, obj in globals().items() if inspect.isfunction(obj)][:-1])

