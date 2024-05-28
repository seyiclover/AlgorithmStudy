import sys
sys.stdin=open('in4.txt','r')

k, n = map(int, input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))

lt = 0
rt = max(nums)

while lt <= rt:
    mid = (lt + rt) // 2

    cnt = 0
    for num in nums:
        cnt += num//mid

    if cnt == n:
        break
    elif cnt > n:
        lt = mid+1
    elif cnt < n:
        rt = mid-1

print(mid)
