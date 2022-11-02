# Reciprocal cycles

def main ():
    max_len = 0
    sol = 0
    for d in range(2,1000):
        now = cycl_len(d) 
        if now > max_len :
            max_len = now
            sol = d
    print(sol)


def cycl_len (n):
    r = []
    div = 1
    while True:    
        if div >= n : r.append(div % n)
        div = (div % n) * 10
        if div % n in r : break
    return len(r) - r.index(div % n)

main ()
