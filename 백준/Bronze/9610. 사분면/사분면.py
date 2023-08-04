first = second = third = fourth = line = 0
for _ in range(int(input())):
    x,y = map(int, input().split())
    if x > 0 and y > 0:
        first += 1
    elif x > 0 and y < 0:
        second += 1
    elif x < 0 and y < 0:
        third += 1
    elif x < 0 and y > 0:
        fourth += 1
    else:
        line += 1

print("Q1:",first)
print("Q2:",fourth)
print("Q3:",third)
print("Q4:",second)
print("AXIS:",line)