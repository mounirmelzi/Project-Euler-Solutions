# solution is 840 ( with a huge ranning time )
biggest = 0
solution = 0
for p in range (1, 1001) :
    #print("p : ",p)
    Counter = 0
    for a in range (1, p ):
        for b in range (a, p ) :
            c = ( a**2 + b**2 ) ** 0.5
            if a+b+c == p : Counter += 1
    if Counter > biggest :
        biggest = Counter
        solution = p

print(solution)
