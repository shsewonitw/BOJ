A,B,C = map(int, input().split())

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

print(prize)