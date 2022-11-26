a,b=map(int,input().split())
g=int((2*a/b)**(2/3))
print(g)
import math
while True:
    if (g+1)*math.sqrt(g)+g*math.sqrt(g+1)<a/b:
        g+=1
    else:
        break
print('{:.10f}'.format(b*(g-1)+a/math.sqrt(g)))