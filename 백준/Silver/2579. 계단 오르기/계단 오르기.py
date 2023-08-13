length = int(input())
stair = [int(input()) for _ in range(length)]

dp = [0] * length

if length < 3:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]
    dp[2] = max(stair[0]+stair[2] , stair[1]+stair[2])
    for i in range(3,length):
        dp[i] = max( dp[i-3] + stair[i-1] + stair[i] , dp[i-2] + stair[i])
        
    print(dp[-1])