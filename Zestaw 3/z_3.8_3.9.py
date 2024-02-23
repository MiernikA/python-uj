L1 = [1, 1, 2, 3, 4, 5]
L2 = [3, 3, 4, 5, 6, 7]
seq = [[], [4], (1, 2), [3, 4], (5, 6, 7)]


S1 = set(L1)
S2 = set(L2)

same_elements = S1.intersection(S2)
all_elements = S1.union(S2)

print("Zadanie 3.8: ")
print(all_elements)
print(same_elements)


sums = [sum(element) for element in seq]

print("Zadanie 3.9: ")
print(sums)