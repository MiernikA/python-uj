# Zadanie 3.1

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# for i in "axby": if ord(i) < 100: print (i)
# for i in "axby": print (ord(i) if ord(i) < 100 else i)

# Nie jest to błąd składniowy, ale nie jest zalecane używanie średników (;) jako separatorów linii.
# W instrukcji warunkowej "if", nawiasy są opcjonalne. Jednak w Pythonie bardziej zaleca się nie używać nawiasów.
# Pętle "for" muszą mieć wcięcie na instrukcje wewnętrzne.


# Poprawiony kod:

print("Zadanie 3.1: ")

x = 2
y = 3

if x > y:
    result = x
else:
    result = y

for i in "axby":
    if ord(i) < 100:
        print(i)

for i in "axby":
    print(ord(i) if ord(i) < 100 else i)


#--------------------------------------------------------------------------------------------------

# Zadanie 3.2

# Co jest złego w kodzie:

# L = [3, 5, 4] ; L = L.sort()
# list.sort() sortuje listę w miejscu i zwraca None.

# x, y = 1, 2, 3
# Trzy wartości do dwóch zmiennych, co jest niepoprawne.

# X = 1, 2, 3 ; X[1] = 4
# Nie można zmieniać wartości w krotce po jej utworzeniu.

# X = [1, 2, 3] ; X[3] = 4
# Indeks 3 wykracza poza zakres listy.

# X = "abc" ; X.append("d")
# .append() jest dostępny tylko dla list, "abc" to string

# L = list(map(pow, range(8)))
# funkcja pow oczekuje dwóch arugmentów

