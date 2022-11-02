def fact (n) : # factorial function
    a=1

    if n==0 : print(n)
    else :
        for i in range(1,n+1):
            a *= i
    
    return a 

result = fact(40) / (fact(20))**2  # 40 C 20
print(int(result))
