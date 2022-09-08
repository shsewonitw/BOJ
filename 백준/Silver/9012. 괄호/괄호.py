import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().rstrip()
    s = []
    isContinue = False
    for char in ps:
        if char == "(":
            s.append(char)
        else:
            if len(s) > 0 and s[-1] == "(":
                s.pop()
            else:
                print("NO")
                isContinue = True
                break
    if isContinue:
        continue
    
    if len(s) == 0:
        print("YES")
    else:
        print("NO")
