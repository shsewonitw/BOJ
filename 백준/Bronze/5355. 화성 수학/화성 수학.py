import math

def calc(result, value):
    if value == '@':
        result *= 3
    elif value == '%':
        result += 5
    elif value == '#':
        result -= 7
    else:
        result += float(value)
        
    return result
        
for _ in range(int(input())):
    exp = input().split()

    # for idx, d in enumerate(exp):
    #     print(idx, d)
    
    result = 0
    
    for d in exp:
        result = calc(result, d)
        
    print('%.2f' %(math.floor(result * 100)/100))