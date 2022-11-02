
def isp (n) : # function return True if input is prime and False if it's not prime .
    if n < 2 : return False 
    if n in (2,3) : return True
    if n%2 == 0 : return False 
    for i in range (3 , (int(n**0.5))+3 , 2) :
        if n%i == 0 : return False 
    return True

def truncatable_prime (n):
    nb_pos = len(str(n))
    #check right to left
    for i in range(0,nb_pos):
        to_check = n // 10**i
        if not isp(to_check) : return False
    #check left to right
    for i in range(1,nb_pos+1):
        to_check = n % 10**i
        if not isp(to_check) : return False
    #After check
    return True
        
sum = 0
counter = 0
num = 11
while counter != 11 :
    if truncatable_prime(num) : 
        sum += num
        counter += 1
    num += 1
print(sum)
