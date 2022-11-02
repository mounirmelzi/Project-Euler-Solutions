def isInteger(n: int) -> bool:
    return n == n // 1
    
def gen_hexagonal(i):
    return i * (2*i - 1)

def isPentagon(k):
    return isInteger((1 + (24*k + 1)**0.5) / 6)

def isTriangle(k):
    return isInteger((-1 + (8*k + 1)**0.5) / 2)

if __name__ == "__main__":
    i = 143
    while True:
        i += 1
        n = gen_hexagonal(i)
        if isPentagon(n) and isTriangle(n):
            print("Solution:", n)
            break
