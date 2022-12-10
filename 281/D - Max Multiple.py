n,k,d=map(int,input().split())
a=list(map(int,input().split()))
import itertools
s=list(sum(_) for _ in itertools.combinations(a,k))
maxs=-1
for _ in s:
    if _%d==0:
        maxs=max(maxs,_)
print(maxs)