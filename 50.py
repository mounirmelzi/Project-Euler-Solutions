def primesGenerator(n: int) -> list[int]:
    primes = []
    visited = [False] * (n + 1)
    for i in range(2, n + 1):
        if not visited[i]:
            primes.append(i)
            for j in range(i ** 2, n + 1, i):
                visited[j] = True
    return primes


LIMIT = 1_000_000
PRIMES: list = primesGenerator(LIMIT)


def isPrime (n: int) -> bool:
    if n < 2 : return False 
    if n == 2 or n == 3 : return True
    if n % 2 == 0 : return False 
    for i in range (3 , (int(n**0.5))+3 , 2) :
        if n % i == 0 : return False 
    return True

def get_serie(prime_index):
    global PRIMES
    global LIMIT
    sum = 0
    max = -1
    counter = 0
    saved_counter = counter
    for i in range(prime_index, len(PRIMES)):
        sum += PRIMES[i]
        if sum > LIMIT:
            break
        counter += 1
        if isPrime(sum):
            saved_counter = counter
            max = sum
    return (max, saved_counter)


if __name__ == "__main__":
    primes_series = []
    for i in range(len(PRIMES)):
        primes_series.append(get_serie(i))

    print("Solution:", max(primes_series, key=lambda x: x[1])[0])
