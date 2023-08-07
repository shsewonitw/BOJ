p1 = p2 = 100
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a > b:
        p2 -= a
    elif a < b:
        p1 -= b
    else:
        continue

print(p1)
print(p2)