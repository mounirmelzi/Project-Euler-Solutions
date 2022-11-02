
def main():
    odd = 3
    while True:
        check = False
        primes = Prime_gen(odd)
        for prime in primes:
            check = isPerfectSquare((odd - prime) / 2)
            if check:
                break
        if not check:
            break
        odd += 2
    print(odd)


def Prime_gen(n):
    primes = []
    visited = [False] * (n + 1)
    for i in range(2, n + 1):
        if not visited[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                visited[j] = True
    return primes

def isInteger(n):
    return n == n // 1

def isPerfectSquare(n):
    return isInteger(n**0.5)



if __name__ == '__main__':
    main()
