# 1, 2, 3, 3, 4


import sys


def plus(li):
    result = 0
    tot = 0

    for num in li:
        result += num 
				# 1, 3, 6, 

        tot += result  
				# 1, 4, 10

    return tot

n = int(sys.stdin.readline()) # 5
nums = sys.stdin.readline(). # 3 1 4 3 2

nums = list(map(int, nums.split())) # [3, 1, 4, 3, 2] type:int
nums = sorted(nums) # [1, 2, 3, 3, 4]

print(plus(nums))
