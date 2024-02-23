def nwd(a, b):
    a = abs(a)
    b = abs(b)

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def reduce_fraction(fraction):
    if fraction[0] == 0:
        return 0



    det = nwd(fraction[0], fraction[1])

    sh_num = fraction[0] // det
    sh_den = fraction[1] // det

    if fraction[1]<0:
        sh_num *= -1
        sh_den *= -1

    return [sh_num, sh_den]


def add_frac(frac1, frac2):
    denominator = frac1[1] * frac2[1] / nwd(frac1[1], frac2[1])
    nominator = frac1[0] * (denominator / frac1[1]) + frac2[0] * (denominator / frac2[1])

    return reduce_fraction([nominator, denominator])


def sub_frac(frac1, frac2):
    denominator = frac1[1] * frac2[1] / nwd(frac1[1], frac2[1])
    nominator = frac1[0] * (denominator / frac1[1]) - frac2[0] * (denominator / frac2[1])

    return reduce_fraction([nominator, denominator])


def mul_frac(frac1, frac2):
    denominator = frac1[1] * frac2[1]
    nominator = frac1[0] * frac2[0]

    return reduce_fraction([nominator, denominator])


def div_frac(frac1, frac2):
    reversed_frac2 = [frac2[1], frac2[0]]
    return mul_frac(frac1, reversed_frac2)


def is_positive(frac):
    if (frac[1] > 0 and frac[0] > 0) or (frac[1] < 0 and frac[0] < 0):
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):
    p1 = frac1[0] * frac2[1]
    p2 = frac2[0] * frac1[1]

    if p1 > p2:
        return 1
    elif p1 == p2:
        return 0
    else:
        return -1


def frac2float(frac):
    return frac[0] / frac[1]


