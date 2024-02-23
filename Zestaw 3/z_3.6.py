height = int(input("Podaj wyokość siatki: "))
width = int(input("Podaj szerokość siatki: "))

mesh = ""
line = "+---"
body = "|   "

for j in range(height * 2+1):
    for i in range(width):
        if j % 2 == 0:
            mesh += line
        else:
            mesh += body
    if j % 2 == 0:
        mesh += "+"
    else:
        mesh += "|"
    mesh += "\n"


print(mesh)
