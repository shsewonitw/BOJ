import sys
from itertools import combinations

height = []

for _ in range(9):
    height.append(int(sys.stdin.readline().rstrip()))
    
for i in combinations(height, 7):
    if(sum(i) == 100):
        i = sorted(i)
        for j in i:
            print(j)
        break