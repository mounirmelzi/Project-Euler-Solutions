
def quad_somme (min, length) :
    u0 = min
    u1 = u0 + ( length - 1 )
    u2 = u1 + ( length - 1 )
    u3 = u2 + ( length - 1 )
    return u0 + u1 + u2 + u3


def calc_max (min, length) :
    return min + 3*length -3


def calc_next_min (min, length) :
    max = calc_max(min, length)
    return max + length + 1


somme = 1
n = 3
for form in range (3, 1001 +1, 2):
    somme += quad_somme (n, form)
    n = calc_next_min(n, form)

print(somme)


