def is_it_abondants (n) :       # function return true if n is abondant
    lis = []

    for i in range ( 1 , int(n**0.5) +1 ) :
        if n%i == 0 :
            lis.append(i)
            lis.append(n//i)
    lis = sorted(list((set(lis))))
    del lis[-1]
    s = sum(lis)
    
    return n<s

abondants = [i for i in range(1,28124) if is_it_abondants(i)]       # listing all abondant <= 28123
to_del =[]

for n in abondants :
    for m in abondants :
        if n+m < 28124 : to_del.append(n+m)     # add the sum between all abondant couple to a list
        else : break
    
to_del = sorted(list(set(to_del)))      # filtering the liste from repetition

print(sum(range(28124))-sum(to_del))        # print sum of all nums - sum of abondant

