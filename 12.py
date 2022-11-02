def triangle_numbers (n) : # n.th triangle number
    n = (n+n**2)/2
    return int(n)


def factors (n) :
    lis = []

    for i in range ( 1 , int(n**0.5) +1 ) :
        if n%i == 0 :
            lis.append(i)
            lis.append(n//i)
    return sorted(list((set(lis))))

i = 0
while len(factors(triangle_numbers(i))) <= 500 :
    i+=1

print(triangle_numbers(i))
