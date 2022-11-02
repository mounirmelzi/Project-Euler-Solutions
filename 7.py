def isp (n) :         # function return True if input is prime and False if it's not prime .
    if n < 2 : return False 
    if n in (2,3) : return True
    if n%2 == 0 : return False 
    for i in range (3 , (int(n**0.5))+3 , 2) :
        if n%i == 0 : return False 
    return True

lis = [2]
i = 3
while len(lis) < 10001 :
    if isp(i) : lis.append(i)
    i += 2

print( "The 10001'st prime number is : " , lis[-1] )
