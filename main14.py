from itertools import combinations_with_replacement

a,b = input().split(maxsplit=1)
y = list(map(str, a))
y.sort()

x = list(combinations_with_replacement(y,int(b)))
x.sort()
for i in x:
    for y in i:
        print(y,end='')
    print()
