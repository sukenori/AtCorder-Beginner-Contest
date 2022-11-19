n=int(input())
a=[int(_) for _ in input().split()]
q=int(input())
for i in range(q):
    qu=[int(_) for _ in input().split()]
    if qu[0]==1:
        a=[qu[1]]*n
    if qu[0]==2:
        a[qu[1]-1]+=qu[2]
    if qu[0]==3:
        print(a[qu[1]-1])