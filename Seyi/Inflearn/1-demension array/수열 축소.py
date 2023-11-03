def compact(nums):
    result = []
    for i in range(len(nums)-1):  # 1~3
        result.append(nums[i+1]-nums[i])

    return result

def solution(nums, m):
    for i in range(m):
        nums = compact(nums)
    return nums

print(solution([5, 3, 7, 9, -2], 2))
