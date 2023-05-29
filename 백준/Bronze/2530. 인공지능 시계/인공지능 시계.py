
hour, min, sec = map(int, input().split())
cookingSec = int(input())

sec += cookingSec

min += sec // 60
sec %= 60

hour += min // 60
min %= 60

hour %= 24

print(hour, min, sec)









