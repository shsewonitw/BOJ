listX = list()
listY = list()

for _ in range(3):
    X,Y = map(int,input().split())

    listX.append(X)
    listY.append(Y)
    
listX.sort()
listY.sort()


for i in range(3):
    if listX.count(listX[i]) == 1:
        resultX = listX[i]
    if listY.count(listY[i]) == 1:
        resultY = listY[i]

print(resultX, resultY)
    
    