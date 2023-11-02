def solution(nums, m): 
    nums = sorted(nums)  
    n = len(nums)
    lt = 0
    rt = n-1

    for i in range(m):
        if nums[lt] < nums[rt]: 
            nums[lt] += 1
            nums[rt] -= 1
        nums = sorted(nums)
        if nums[lt] == nums[rt]:
            return 0
    
    return max(nums) - min(nums)

print(solution([2, 1, 3, 7, 5], 2))
print(solution([69, 42, 68, 76, 40, 87, 14, 65, 76, 81], 50))
print(solution([3, 2, 3, 3, 4], 3))
