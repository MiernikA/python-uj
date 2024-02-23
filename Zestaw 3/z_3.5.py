measure_len = int(input("Podaj długość miarki: "))
measure = ""
block = "|...."


def distance_for_num(n):
    if n == 0:
        return str(n)

    distance = 0
    tmp = n
    while n > 0:
        distance += 1
        n //= 10

    whitespace = ""
    for z in range(5 - distance):
        whitespace += " "

    return whitespace + str(tmp)


for i in range(measure_len):
    measure += block

measure += "|\n"

for j in range(measure_len + 1):
    measure += distance_for_num(j)

print(measure)
