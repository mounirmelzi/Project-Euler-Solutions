
def main():
    solution = 0
    for number in range(3, 40585 + 1):
        if verified(number):
            solution += number
    print(solution)


def factorial(n):
    if (n == 1) or (n == 0):
        return 1
    return n * factorial(n - 1)


def verified(a):
    sum = 0
    for digit in str(a):
        sum += factorial(int(digit))
    return (sum == a)



if __name__ == '__main__':
    main()
