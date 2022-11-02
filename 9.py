# a² + b² = c²
# a + b + c = 1000
# a < b < c

for a in range (1,1000) : 
    for b in range (1 , 1000)  :
        c = ( a**2 + b**2 )**0.5
        if c%1==0 and a+b+c==1000 and a<b<c :
            print(int(a*b*c))
