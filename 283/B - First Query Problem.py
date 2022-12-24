n=int(input())
a=list(map(int,input().split()))
q=int(input())
for i in range(q):
    qi=list(input().split())
    if qi[0]=="1":
        a[int(int(qi[1]))-1]=int(qi[2])
    if qi[0]=="2":
        print(a[int(qi[1])-1])