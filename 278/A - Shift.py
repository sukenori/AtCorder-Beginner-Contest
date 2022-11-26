n,k=map(int,input().split())
a=[int(_) for _ in input().split()]
for i in range(k):
    a.pop(0)
    a.append(0)
a=[str(i) for i in a]
print(" ".join(a))