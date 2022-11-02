s='0123456789'
lis=[]

for a in s :
    if len(lis)==1000000 : break
    s1 = s.replace(a,'')

    for b in s1 :
        if len(lis)==1000000 : break
        s2 = s1.replace(b,'')

        for c in s2 :
            if len(lis)==1000000 : break
            s3 = s2.replace(c,'')

            for d in s3 :
                if len(lis)==1000000 : break
                s4 = s3.replace(d,'')

                for e in s4 :
                    if len(lis)==1000000 : break
                    s5 = s4.replace(e,'')

                    for f in s5 :
                        if len(lis)==1000000 : break
                        s6 = s5.replace(f,'')

                        for g in s6 :
                            if len(lis)==1000000 : break
                            s7 = s6.replace(g,'')

                            for h in s7 :
                                if len(lis)==1000000 : break
                                s8 = s7.replace(h,'')

                                for i in s8 :
                                    if len(lis)==1000000 : break
                                    s9 = s8.replace(i,'')

                                    for j in s9 :
                                        if len(lis)==1000000 : break
                                        lis.append( str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j) )
                                        
                
print( ( sorted (lis) ) [-1] )


