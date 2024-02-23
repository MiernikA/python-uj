def odwracanie_iteracyjnie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left = left + 1
        right = right - 1


def odwracanie_rekurencyjnie(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjnie(L, left + 1, right - 1)


# Example usage
example_array = [1, 2, 3, 4, 5, 6]
odwracanie_iteracyjnie(example_array, 1, 4)
print(example_array)  # 1,5,4,3,2,6
odwracanie_rekurencyjnie(example_array, 0, 5)
print(example_array)  # 6,2,3,4,5,1
