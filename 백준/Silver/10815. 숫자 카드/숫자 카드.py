from bisect import bisect_left, bisect_right
N = int(input())
nums = list(map(int,input().split()))
nums.sort()
M = int(input())
nums_question = list(map(int,input().split()))

result = []

for i in nums_question:
    if( (bisect_right(nums, i) - bisect_left(nums, i)) != 0):
        result.append(1)
    else:
        result.append(0)
        


for idx , val in enumerate(result):
    if(idx == len(result) - 1):
        print(val)
    else:
        print(val, end=" ")