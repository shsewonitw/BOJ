import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

MOD = 10_007

n = int(input())

dp = [0] * 1001

# Top-Down
# def getCount(idx):
#     if dp[idx] != 0:
#         return dp[idx]
    
#     if idx == 1:
#         dp[idx] = 1
#         return dp[idx]
#     elif idx == 2:
#         dp[idx] = 2
#         return dp[idx]
    
#     dp[idx] = (getCount(idx-1) + getCount(idx-2)) % MOD
#     return dp[idx]

# print(getCount(n))

# Bottom-Up

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
print(dp[n])