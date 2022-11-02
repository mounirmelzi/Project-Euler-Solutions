
# Project Euler 30
# Digit fifth powers !!

def checker(num):
    return num == sum(int(x)**5 for x in str(num))

if __name__ == '__main__':
    print(sum((x for x in range(2, 194979+1) if checker(x))))
