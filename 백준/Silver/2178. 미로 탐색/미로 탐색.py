from collections import deque

N,M = map(int, input().split())

board = [input() for _ in range(N)]

chk = [[False] * M for _ in range(N)]


dy = (0,1,0,-1)
dx = (1,0,-1,0)

def isRightLocation(y, x):
    return (y >= 0 and y < N and x >= 0 and x < M)

def bfs():
    chk[0][0] = True
    dq = deque()
    dq.append((0,0,1))
    while dq:
        y, x, r = dq.popleft()
        
        if y == N-1 and x == M-1:
            return r

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            nr = r + 1
            if isRightLocation(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny,nx, nr))
                
    
print(bfs())