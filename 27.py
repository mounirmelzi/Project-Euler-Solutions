def isp (n) : # function return True if input is prime and False if it's not prime .
    if n < 2 : return False 
    if n in (2,3) : return True
    if n%2 == 0 : return False 
    for i in range (3 , (int(n**0.5))+3 , 2) :
        if n%i == 0 : return False 
    return True

# n² + an + b  : should be prime
# -1000 < a < 1000
# -1000 <= b <= 1000

max = { 'a' : 0   ,  'b' : 0 }
count = 0
biggest = 0

for a in range (-999 , 1000) :
    for b in range (-1000 , 1000) :

        n = 0
        while isp( n**2 + a*n +b ) :
            count += 1
            n += 1
        
        if count > biggest : 
            biggest = count
            max['a'] = a
            max['b'] = b
         
        count = 0

print (max['a'] * max['b'])

