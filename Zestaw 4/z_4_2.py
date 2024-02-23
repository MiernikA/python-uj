def distance_for_num(x):
    if x == 0:
        return str(x)

    distance = 0
    tmp = x
    while x > 0:
        distance += 1
        x //= 10

    whitespace = ""
    for z in range(5 - distance):
        whitespace += " "

    return whitespace + str(tmp)


def make_ruler(n):
    measure = ""
    block = "|...."

    for i in range(n):
        measure += block

    measure += "|\n"

    for j in range(n + 1):
        measure += distance_for_num(j)

    return measure


# -----


def make_grid(rows, cols):
    mesh = ""
    line = "+---"
    body = "|   "

    for j in range(rows * 2 + 1):
        for i in range(cols):
            if j % 2 == 0:
                mesh += line
            else:
                mesh += body
        if j % 2 == 0:
            mesh += "+"
        else:
            mesh += "|"
        mesh += "\n"

    return mesh


# Example usage
print(make_ruler(5))
print("#-------------------------------------#")
print(make_grid(2, 3))
