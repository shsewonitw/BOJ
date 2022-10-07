N,L = map(int, input().split())


holes = list(map(int, input().split()))

result = 0
target = 0
for hole in sorted(holes):

    if hole <= target:
        continue

    result += 1
    target = hole + L - 1
    
    
print(result)