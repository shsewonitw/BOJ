cute = 0
notCute = 0
for _ in range(int(input())):
    n = int(input())
    if n:
        cute += 1
    else:
        notCute += 1

if cute > notCute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")