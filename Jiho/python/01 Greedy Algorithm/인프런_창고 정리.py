# 창고 정리

l = int(input())
nums = list(map(int, input().split()))
m = int(input())

# 큰 순서대로 정리
for i in range(m):
    nums.sort()
    nums[0] += 1
    nums[-1] -= 1

print(max(nums) - min(nums))
