for _ in range(int(input())):
    sumY = sumK = 0
    for _ in range(9):
        y,k = map(int,input().split())
        sumY += y
        sumK += k
    if sumY > sumK:
        print("Yonsei")
    elif sumY < sumK:
        print("Korea")
    else:
        print("draw")