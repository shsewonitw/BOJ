while True:
    n = int(input())
    if n == -1:
        break
    
    ys = [1]
    for i in range(2,n):
        if i in ys:
            break
        if n % i == 0:
            ys.append(i)
            ys.append(int(n/i))
    ys.sort()
    
    # 완전수
    if sum(ys) == n:
        print(f'{n}', end=' =')
        for i in ys:
            print(f' {i}', end='')
            if ys[-1] == i:
                print('')
                break
            print(' +', end='')
    else:
        print(f'{n} is NOT perfect.')