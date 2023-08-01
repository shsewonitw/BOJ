str = input()
length = 0
for i,c in enumerate(str):
    if i == 0 or str[i-1] != c:
        length += 10
    else:
        length += 5
print(length)