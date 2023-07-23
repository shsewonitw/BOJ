S = int(input())

sum = 0
num = 1
idx = 0

while True:
    idx += 1
    sum += num
    num+=1
    if sum == S:
        break
    elif sum > S:
        idx -= 1
        break

print(idx)