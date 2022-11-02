def main():
    max = 0
    for i in range(100000):
        n = generatePandigitalMultiples(i)
        if n is not None and n > max: max = n
    print("Solution: ", max)

def isPandigital(n: int) -> bool:
    return "123456789" == "".join(sorted(str(n)))

def generatePandigitalMultiples(number):
    s = ""
    n = 1
    while len(s) < 9:
        s += str(number * n)
        n += 1
    n = int(s)
    return n if isPandigital(n) else None

if __name__ == "__main__":
    main()
