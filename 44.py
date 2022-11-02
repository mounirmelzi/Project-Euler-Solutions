
# Math approach solution:
    # Pn = n(3n-1)/2 = k  |  k is an integer >= 1
    # --> n = (1 + sqrt(24k+1)) / 6  |  n is an integer >= 1

    # Pi + Pj = ((i+j) / 2) * (3 * ((i²+j²) / (i+j)) - 1)
    # Pi - Pj = ((i-j) / 2) * (3*(i+j) - 1)

    # d(Pi-Pj)/di = 3i - 0.5 > 0 : because i >= 1   -> to get min(Pi-Pj) we should minimize i 
    # d(Pi-Pj)/dj = -3j + 0.5 < 0 : because j >= 1  -> to get min(Pi-Pj) we should maximaze j

    # We should always keep this condition: i > j



def isInteger(n: int) -> bool:
    return n == n // 1


def isPentagon(k):
    return isInteger((1 + (24*k + 1)**0.5) / 6)


def sumPentagon(i, j):
    return int(((i+j) / 2) * (3 * ((i**2 + j**2) / (i+j)) - 1))


def diffPentagon(i, j):
    return abs(int(((i-j) / 2) * (3*(i+j) - 1)))


if __name__ == "__main__":
    i = 1 # Minimize i
    Continue = True
    while Continue:
        for j in range(i-1, 1, -1): # Maximaze j and we must always have i > j
            if isPentagon(sumPentagon(i, j)) and isPentagon(diffPentagon(i, j)):
                print("Solution:", diffPentagon(i, j))
                Continue = False
                break
        i += 1
