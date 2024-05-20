# 선택 정렬

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))


# 15 27 12
for i in range(n):
    mi = i
    for j in range(i+1, n):
        if nums[mi] < nums[j]:
            mi = j
    nums[i], nums[mi] = nums[mi], nums[i]

print(nums)


## 정답
n = int(input())
array = []
for i in range(n):
		array.append(int(input())
		
array = sorted(array, reverse=True)

for i in array:
		print(i, end=' ')
