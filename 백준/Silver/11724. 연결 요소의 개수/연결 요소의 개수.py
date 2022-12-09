import sys

sys.setrecursionlimit(10**6)
N,M = map(int, sys.stdin.readline().rstrip().split())

adj = [[0] * N for _ in range(N)]


for _ in range(M):
    u,v = map(lambda x: x-1, map(int, sys.stdin.readline().rstrip().split()))
    adj[u][v] = 1
    adj[v][u] = 1

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)