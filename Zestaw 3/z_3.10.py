roman_to_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman2int(roman):
    total = 0
    prev_value = 0

    for digit in roman[::-1]:
        value = roman_to_arabic[digit]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


roman_num = input("Podaj liczbe rzymska: ")
print(roman2int(roman_num))
