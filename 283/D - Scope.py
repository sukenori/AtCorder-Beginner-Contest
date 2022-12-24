s=input()
b=[set()]
for i in s:
    if i=="(":
        b.append(set())
        continue
    if i==")":
        b.pop(-1)
        continue
    for j in b:
        if i in j:
            print("No")
            exit()
    else:
        b[-1].add(i)
        continue
else:
    print("Yes")