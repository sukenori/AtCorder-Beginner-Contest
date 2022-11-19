n,q=map(int,input().split())
t=[list(map(int,input().split())) for _ in range(q)]
ff=[[0 for i in range(n)] for j in range(n)]
for i in range(q):
    if t[i][0]==1:
        ff[t[i][1]-1][t[i][2]-1]=1
    if t[i][0]==2:
        ff[t[i][1]-1][t[i][2]-1]=0
    if t[i][0]==3:
        if ff[t[i][1]-1][t[i][2]-1]==1 and ff[t[i][2]-1][t[i][1]-1]==1:
            print("Yes")
        else:
            print("No")