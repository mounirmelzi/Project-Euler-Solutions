def re (x) :   # function to reverse digits
    a=str(x)
    b=a[::-1]
    return int(b)

my_list = []
for p in range (100 , 1000):
    for q in range (100 , 1000):

            if q*p == re(q*p) :
               my_list.append(q*p)
    
print (  max(my_list)  )
