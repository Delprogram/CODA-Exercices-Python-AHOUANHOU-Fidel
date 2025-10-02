# Exemple avec un seul exercice
def exercise0():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercise1():
    print("Bonjour tout le monde !")

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choice = input("Entrez le numéro de l'exercice à exécuter : ")
    if choice == "1":
        exercise1()
    else:
        print("Exercice non reconnu.")


if __name__ == "__main__":
        main()