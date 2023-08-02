V = int(input())
S = input()

len_A = 0
len_B = 0

for c in S:
    if c == 'A':
        len_A += 1
    else:
        len_B += 1

if len_A == len_B:
    print('Tie')
elif len_A > len_B:
    print('A')
else:
    print('B')