import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().rstrip()
    s = []
    isVPS = True
    for char in ps:
        if char == "(":
            s.append(char)
        else:
            if len(s) > 0 and s[-1] == "(":
                s.pop()
            else:
                isVPS = False
                break

    
    if len(s) > 0:
        isVPS = False
    print('YES' if isVPS else 'NO')