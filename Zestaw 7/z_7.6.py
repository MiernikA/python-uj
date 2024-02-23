import random


class IteratorA:
    def __init__(self):
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value == 0:
            self.current_value = 1
        else:
            self.current_value = 0

        return self.current_value


class IteratorB:

    def __init__(self):
        self.current_value = "N"

    def __iter__(self):
        return self

    def __next__(self):
        arr = ["N", "S", "W", "E"]
        direction = random.choice(arr)
        return direction


class IteratorC:

    def __init__(self):
        self.current_value = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_value +=1
        if self.current_value == 7:
            self.current_value = 0
        return self.current_value


it_a = IteratorA()
it_b = IteratorB()
it_c = IteratorC()

print("7.6 a:")
for _ in range(10):
    print(next(it_a), end=" ")

print("\n7.6 b:")
for _ in range(10):
    print(next(it_b), end=" ")

print("\n7.6 c:")
for _ in range(10):
    print(next(it_c), end=" ")