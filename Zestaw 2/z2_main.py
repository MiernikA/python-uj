# DANE
line = "Testowy tekst    odzielony\nróżnymi  znakami GvR"
word = "word"

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
L2 = [1, 22, 333, 4, 55, 666, 7, 88, 999, 0]

huge_number = 7391040124812479000


# Zadanie 2.10
words = line.split()
print("2.10:", len(words))


# Zadanie 2.11
new_word = '_'.join(word)
print("2.11:", new_word)


# Zadanie 2.12
words = line.split()
txt_by_first = ""
txt_by_last = ""
for word in words:
    txt_by_first += word[0]
    txt_by_last += word[len(word) - 1]

print("2.12 (by first):", txt_by_first)
print("2.12 (by last):", txt_by_last)


# Zadanie 2.13
words = line.split()
all_words_length = sum(len(word) for word in words)

print("2.13:", all_words_length)


# Zadanie 2.14
words = line.split()
longest_word = max(words, key=len)
longest_word_length = len(longest_word)

print("2.14:", longest_word, longest_word_length)


# Zadanie 2.15
word = ""
for num in L:
    word += str(num)

print("2.15:", word)


# Zadanie 2.16
new_line = line.replace("GvR","Guido van Rossum")
print("2.16:", new_line)


# Zadanie 2.17
words = line.split()
alphabetic_sort = sorted(words)
length_sort = sorted(words, key=len)

print("2.17 (by alph):", alphabetic_sort)
print("2.17 (by len):", length_sort)


# Zadanie 2.18
string_num = str(huge_number)
amount_of_zeros = string_num.count('0')
print("2.18:", amount_of_zeros)


# Zadanie 2.19
word = ""
for num in L2:
    op = str(num)
    txt = op.zfill(3)
    word += txt

print("2.19:", word)
