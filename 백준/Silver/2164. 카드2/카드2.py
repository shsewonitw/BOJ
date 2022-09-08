import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

dq = deque()

for i in range(N):
    dq.append(i+1)
    
while True:
    if len(dq) == 1:
        break
    
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq[0])
    