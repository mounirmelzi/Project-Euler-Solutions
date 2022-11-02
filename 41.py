# n != 1 2 3 5 6 8 9
# n = 4 ou 7

def isp (n) : # function return True if input is prime and False if it's not prime .
    if n < 2 : return False 
    if n in (2,3) : return True
    if n%2 == 0 : return False 
    for i in range (3 , (int(n**0.5))+3 , 2) :
        if n%i == 0 : return False 
    return True

ls = []

# n = 4 
# assurer que les digits des nombres à checker soient (<= 4) et (!= 0)
for i in range( 2341 , 4321+1 , 2 ) :
    c = False
    for p in str(i) :
        if int(p) > 4 or int(p) == 0  :
            c = True
            break
    if c : continue
# this IFs to eleminate double digits
    i = str(i)
    if not ( i[0] != i[1] != i[2] != i[3] ) : continue
    if not ( i[1] != i[3] != i[0] != i[2] ) : continue
# check if i is prime to add it to the liste   
    if isp(int(i)) : 
        ls.append(i)
#        print(i)


# n = 7
# assurer que les digits des nombres à checker soient (<= 7) et (!= 0)
for i in range( 1234567 , 7654321+1 , 2 ) :
    c = False
    for p in str(i) :
        if int(p) > 7 or int(p)==0 :
            c = True
            break
    if c : continue
# this IFs to eleminate double digits
    i = str(i)
    if not ( i[1] != i[0] != i[4] != i[0] != i[1] != i[4] ) : continue
    if not ( i[2] != i[0] != i[5] != i[2] != i[1] != i[5] ) : continue
    if not ( i[3] != i[0] != i[6] != i[3] != i[1] != i[6] ) : continue
    if not ( i[2] != i[3] != i[4] != i[5] != i[3] ) : continue
    if not ( i[2] != i[4] != i[6] ) : continue
    if not ( i[2] != i[6] != i[5]  ) : continue
# check if i is prime to add it to the liste 
    if isp(int(i)) : 
        ls.append(i)
#        print(i)


print(ls[-1])
