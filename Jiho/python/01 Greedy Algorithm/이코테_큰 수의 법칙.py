N, M = map(int, input().split())
x = []; mins = []

for i in range(N):
    nums = list(map(int, input().split()))
    mins.append(min(nums))
    x.append(nums)

print(max(mins))
