s='0123456789'
lis=[]

for a in s :
    s1 = s.replace(a,'')

    for b in s1 :
        s2 = s1.replace(b,'')

        for c in s2 :
            s3 = s2.replace(c,'')

            for d in s3 :
                s4 = s3.replace(d,'')

                for e in s4 :
                    s5 = s4.replace(e,'')

                    for f in s5 :
                        s6 = s5.replace(f,'')

                        for g in s6 :
                            s7 = s6.replace(g,'')

                            for h in s7 :
                                s8 = s7.replace(h,'')

                                for i in s8 :
                                    s9 = s8.replace(i,'')

                                    for j in s9 :
                                        lis.append( str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j) )
                                        
c = 0        
for num in lis :
    if int(num[1:4]) % 2 == 0 :
        if int(num[2:5]) % 3 == 0 :
            if int(num[3:6]) % 5 == 0 :
                if int(num[4:7]) % 7 == 0 :
                    if int(num[5:8]) % 11 == 0 :
                        if int(num[6:9]) % 13 == 0 :
                            if int(num[7:10]) % 17 == 0 :
                                c += int(num)

print(c)

