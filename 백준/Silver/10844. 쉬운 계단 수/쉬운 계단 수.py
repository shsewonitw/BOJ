import sys

input = sys.stdin.readline
MOD = 1_000_000_000
sys.setrecursionlimit(10**9)

N = int(input())

# dp = [[-1]* 10] * 101
dp = [[-1]* 10 for _ in range(101)]
dp[1][0] = 0
for i in range(1,10):
    dp[1][i] = 1

def getStairNumber(idx, d):
    if dp[idx][d] != -1:
        return dp[idx][d]
    
    if d == 9:
        dp[idx][d] = getStairNumber(idx - 1, d - 1) % MOD
    elif d == 0:
        dp[idx][d] = getStairNumber(idx - 1, d + 1) % MOD
    else:
        dp[idx][d] = ( getStairNumber(idx - 1, d + 1) + getStairNumber(idx - 1, d - 1) ) % MOD
    
    return dp[idx][d]
    
sum = 0
for i in range(0,10):
    sum += getStairNumber(N,i)
    sum %= MOD
    
print(sum)