## 내 풀이
# 입력 
n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

comp = []
# 행의 합 
for i in range(n):
    comp.append(sum(nums[i]))

# 열의 합
for i in range(n):
    tot = 0
    for j in range(n):
        tot += nums[j][i]
    comp.append(tot)

# 우하강 대각선 합
tot = 0
for i in range(n):
    tot+=nums[i][i]
comp.append(tot)

# 우상향 대각선 합
tot=0
for i in range(n):
    for j in range(4, -1, -1):
        if i+j==n-1:
            tot+=nums[i][j]
comp.append(tot)

print(max(comp))



## 정답풀이 

# n 입력 
n = int(input())

# 2차원 리스트 입력
a= [list(map(int, input().split())) for _ in range(n)]

# 행, 열의 합의 최댓값 찾기 
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]   # 행 고정 열 반복 -> 행의 합
        sum2+=a[j][i]   # 열 고정 행 반복 -> 열의 합
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

# 대각선 합 비교
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

print(largest)
