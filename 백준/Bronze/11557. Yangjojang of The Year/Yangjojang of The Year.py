for _ in range(int(input())):
    univDict = {}
    for _ in range(int(input())):
        univ, score = input().split()
        univDict[univ] = int(score)
    print(max(univDict,key=univDict.get))