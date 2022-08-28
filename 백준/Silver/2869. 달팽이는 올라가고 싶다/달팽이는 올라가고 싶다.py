A, B, V = map(int, input().split())

result = 0
if(V == A):
  result = 1
else:
  up = A - B
  result = (V - A) / up + 1
  if((V - A)%up != 0):
    result = result + 1
print(int(result))