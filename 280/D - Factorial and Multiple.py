k=int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

d=make_divisors(k)
e=[d[0],d[len(d)-1]]
c=1
while c==1:
    c=0
    for _ in e:
        for i in d:
            for j in d:
                print(e)
                if _==i*j and i!=1 and j!=1:
                    e.remove(_)
                    e.append(i)
                    e.append(j)
                    c=1
print(e)