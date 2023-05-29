
hour, min = map(int, input().split())
cookingMin = int(input())

min += cookingMin
hour += ( min // 60 )

min %= 60
hour %= 24

print(hour, min)