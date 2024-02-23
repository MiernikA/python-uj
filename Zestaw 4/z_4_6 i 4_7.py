# 4.6
def sum_seq(sequence):
    sum = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            sum += sum_seq(element)
        else:
            sum += element
    return sum


# 4.7
def flatten(sequence):
    product = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            for el in flatten(element):
                product.append(el)

        else:
            product.append(element)

    return product


# Example usage
seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]  # 1+2+3+4+5+6+7+8+9=45

print(sum_seq(seq))
print(flatten(seq))
