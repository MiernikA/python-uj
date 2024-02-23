while True:
    x = input("Podaj liczbę rzeczywistą (lub 'stop' aby zakończyć): ")

    if x =="stop":
        break

    try:
        x = float(x)
        print("> ",x,"^ 3 = ", pow(x,3))

    except ValueError:
        print("To nie jest liczba rzeczywista")




