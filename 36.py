
def re (x) :   # function to reverse digits
    a=str(x)
    b=a[::-1]
    return int(b)

def dec_to_bin (n) :
    d=i=0
    while n != 0 :
        d += (n%2)*(10**i)
        i+=1
        n = n//2
    return d

somme = 0
for i in range (1000000) : 
    if i==re(i) and dec_to_bin(i)==re(dec_to_bin(i)) : somme += i
print(somme)
