def getPrimeFactors(num: int) -> list[tuple[int, int]]:
    if num <= 0:
        return None

    prime_factors = []

    counter = 0
    while num % 2 == 0:
        counter += 1
        num = num // 2
    if counter != 0:
        prime_factors.append((2, counter))

    for i in range(3, int(num ** 0.5) + 1, 2):
        counter = 0
        while num % i == 0:
            counter += 1
            num = num // i
        if counter != 0:
            prime_factors.append((i, counter))

    if num > 2:
        prime_factors.append((num, 1))

    return prime_factors

number = 1
while True:
    numbers = [number + i for i in range(4)]
    prime_factors = [getPrimeFactors(number) for number in numbers]

    condition = (
        all(len(primes) == 4 for primes in prime_factors)
        and
        prime_factors[0] != prime_factors[1] and prime_factors[0] != prime_factors[2] and prime_factors[0] != prime_factors[3]
        and
        prime_factors[1] != prime_factors[2] and prime_factors[1] != prime_factors[3]
        and
        prime_factors[2] != prime_factors[3]
    )

    if condition:
        break
    number += 1

print("Solution:", number)
