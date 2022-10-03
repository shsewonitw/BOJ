import sys
import heapq

N = int(sys.stdin.readline().rstrip())

dict = {}
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    dict[name] = dict[name] + 1 if name in dict else 1
    
# sorted_dict = sorted(dict.items(), key = lambda item: item[0])


sorted_dict = sorted(dict.items(), key = lambda item: (-item[1],item[0]))



print(next(iter(sorted_dict))[0])