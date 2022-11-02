
def main():
    primelist = Prime_gen(9999)
    primelist = [ x for x in primelist if len(str(x))==4 ]
    for i in primelist:
        if isp(i) and isp(i+3330) and isp(i+6660) and same_digits(i,i+3330) and same_digits(i,i+6660) and i!=1487:
            print(i,i+3330,i+6660, sep='')
            break


def isp (n) :
    if n < 2 : return False 
    if n in (2,3) : return True
    if n%2 == 0 : return False 
    for i in range (3 , (int(n**0.5))+3 , 2) :
        if n%i == 0 : return False 
    return True

def Prime_gen(n):
    primes = []
    visited = [False] * (n + 1)
    for i in range(2, n + 1):
        if not visited[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                visited[j] = True
    return primes

def same_digits(x, y: int) -> bool:
    return sorted(str(x)) == sorted(str(y))



if __name__ == '__main__':
    main()
