for _ in range(int(input())):
    score = 0
    add = 0
    str = input()
    for c in str:
        if c == 'O':
            add += 1
            score += add
        else:
            add = 0
    print(score)