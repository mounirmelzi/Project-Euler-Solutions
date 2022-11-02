possibilities = set()


def isPandigitalProduct(a, b):
    global possibilities

    if sorted(str(a) + str(b) + str(a * b)) == [str(c) for c in range(1, 10)]:
        possibilities.add(a * b)


def main():
    for a in range(1, 10):
        for b in range(1000, 10000):
            isPandigitalProduct(a, b)

    for a in range(10, 100):
        for b in range(100, 1000):
            isPandigitalProduct(a, b)

    print("Solution:", sum(possibilities))


if __name__ == "__main__":
    main()
