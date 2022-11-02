
ls = []
for a in range (2 , 101 ) :
    for b in range ( 2 , 101 ) :
        ls.append(a**b)
print(len(set(ls)))


# ls = []
# for a in range (2 , 101 ) :
#     for b in range ( 2 , 101 ) :
#         if a**b not in ls : ls.append(a**b)
# print(len(ls))

