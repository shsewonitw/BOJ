import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

MOD = 10_007

n = int(input())

dp = [0] * 1001

def getCount(idx):
    if dp[idx] != 0:
        return dp[idx]
    
    if idx == 1:
        dp[idx] = 1
        return dp[idx]
    elif idx == 2:
        dp[idx] = 2
        return dp[idx]
    
    dp[idx] = (getCount(idx-1) + getCount(idx-2)) % MOD
    return dp[idx]

print(getCount(n))