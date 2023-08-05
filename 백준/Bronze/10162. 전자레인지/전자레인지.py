times = [300, 60, 10]
T = int(input())
if T % times[-1] != 0:
    print(-1)
    exit()

result = list()
for time in times:
    result.append(T//time)
    T = T%time

print(' '.join(str(i) for i in result))