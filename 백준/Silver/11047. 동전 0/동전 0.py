import sys

N, K = map(int ,sys.stdin.readline().rstrip().split())

A = []
result = 0
for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip()))
    
for i in reversed(A):
    result += K // i
    K %= i
    
print(result)