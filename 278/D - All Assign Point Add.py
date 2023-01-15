n=int(input())
a=list(map(int,input().split()))
q=int(input())
qu=[list(map(int,input().split())) for i in range(q)]
for i in range(q):
    if qu[i][0]==3:
        add=0
        for j in reversed(range(i+1)):
            if qu[j][0]==2 and qu[j][1]==qu[i][1]: add+=qu[j][2]
            if j==0:
                print(a[qu[i][1]-1]+add)
                break
            elif qu[j][0]==1:
                print(qu[j][1]+add)
                break