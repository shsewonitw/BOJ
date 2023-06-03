for _ in range(int(input())):
    R, S = input().split()
    for c in S:
        print(c*int(R), end="")
    print()