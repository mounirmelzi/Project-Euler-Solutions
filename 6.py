list_a = []
list_b = []


for i in range ( 1 , 101 ) :
    list_a.append(i**2)
a = sum(list_a)

for j in range ( 1 , 101 ) :
    list_b.append(j)
b = ( sum(list_b) )**2

print("result is : " , abs(b-a))
