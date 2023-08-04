s = input()

flag = 1

for i, c in enumerate(s):
    if i == len(s)-1-i:
        break
    if c != s[len(s)-1-i]:
        flag = 0
        break

print(flag)