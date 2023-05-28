T = int(input())

for idx in range(T):
    A,B = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(idx+1, A,B,A+B))
    