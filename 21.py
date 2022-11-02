def somme_dev (n) :
    lis = []

    for i in range ( 1 , int(n**0.5) +1 ) :
        if n%i == 0 :
            lis.append(i)
            lis.append(n//i)

    lis = sorted(list(set(lis)))
    return sum(lis)-n

c = 0
for i in range(0 , 10000) :
    if somme_dev(somme_dev(i)) == i and somme_dev(i) != i:
        c += i

print(c)
