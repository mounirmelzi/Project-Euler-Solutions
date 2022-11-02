def isp (n) : # function return True if input is prime and False if it's not prime .
    if n < 2 : return False 
    if n in (2,3) : return True
    if n%2 == 0 : return False 
    for i in range (3 , (int(n**0.5))+3 , 2) :
        if n%i == 0 : return False 
    return True



def rect (k) :   # geniuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuss  ----> circular numbers
    k = str(k)
    l = len(k)
    ll =[]
  
    for i in range(l) :
        kk = k[i:]+k[:i]
        ll.append(int(kk))

    return ll



#--------------------------------

prime_liste = [2]
for i in range(3,1000000,2) :
    if isp (i) :
        prime_liste.append(i)

#--------------------------------


Counter = 0
for num in prime_liste :
    for c in rect(num) :
        if not isp(c) : break
    else:
        Counter += 1

print(Counter)
