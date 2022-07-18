import itertools


from itertools import groupby
if __name__ == '__main__':
    a = input()

for k, g in groupby(a):
    mytuple = (len(list(g)),int(k))
    print(mytuple,end=' ')
