def getPrize(A,B,C):
    prize = 0

    if A == B == C:
        prize = 10000 + A * 1000
    elif A == B != C:
        prize = 1000 + A * 100
    elif B == C != A:
        prize = 1000 + B * 100
    elif A == C != B:
        prize = 1000 + C * 100
    else:
        prize = max(A,B,C) * 100

    return prize

maxPrize = 0
for _ in range(int(input())):
    A,B,C = map(int,input().split())
    prize = getPrize(A,B,C)
    maxPrize = prize if prize > maxPrize else maxPrize
    
print(maxPrize)