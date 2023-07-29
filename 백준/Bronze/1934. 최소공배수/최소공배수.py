def gcd(num1, num2):
    if num1 > num2:
        num1 , num2 = num2, num1
    
    while True:
        if num2 % num1 == 0:
            return num1
        
        num1, num2 = num2 % num1 , num1
        
for _ in range(int(input())):
    A,B = map(int, input().split())
    print(int(A*B / gcd(A,B)))