s = '0'
i = 1
while len(s) <= 1000000 :
    s=s+str(i)
    i+=1

sum = int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])
print(sum)
