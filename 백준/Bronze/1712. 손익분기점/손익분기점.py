A, B, C = map(int, input().split())
result = 0

if(B >= C):
    result = -1
else:
  benefit = C - B
  result = A / benefit + 1

print(int(result))