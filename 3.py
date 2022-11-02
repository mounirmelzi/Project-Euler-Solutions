x = 600851475143
p = 2

while x != p :

    while x%p ==0 and x != p :
        x = x / p
    else :
        p += 1

print(int(x))
