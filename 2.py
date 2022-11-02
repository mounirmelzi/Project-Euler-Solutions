l = [1,1,2]
my_list = []

k=0
while k <= 4000000 :

    xf = len(l) - 1
    xff = xf - 1

    a = l[xf]   # the last element in the liste
    b = l[xff]  # the element previous the last one 

    k = a + b
    if k <= 4000000 : l.append(k) 

print("the fibonacci numbers are : " ,l)

for n in range(0 , len(l)) :
    if l[n]%2 == 0 :
        my_list.append(l[n])

print("the even fibonacci numbers are : " , my_list)

print( "the final result is : ",sum(my_list))
