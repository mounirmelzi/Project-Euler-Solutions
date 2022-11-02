def check ( n ) :
    if n%2==0 : return n/2
    else : return (3*n)+1

lis = []
counter =0
biggest = 0

for x in range(500001 , 999999 , 2):
    t = x

    while x != 1 :
        x=check(x)
        counter += 1

    if counter > biggest : 
        biggest = counter 
        lis.append(t)

    counter = 0

print(lis[-1])
