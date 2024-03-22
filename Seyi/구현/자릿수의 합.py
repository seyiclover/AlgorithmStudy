# 입력 
n = int(input())
nums = list(map(int, input().split()))
nums_sum = []

# 자릿수 합 계산 함수
def digit_sum(x):
    x = str(x)
    x_sum = 0
    for i in x:
        x_sum += int(i)
    nums_sum.append(x_sum)

for x in nums:
    digit_sum(x)

# 자릿수 합의 최대값
max_sum = max(nums_sum)
# 최대값 인덱스 
idx = nums_sum.index(max_sum)
# 자릿수 합이 가장 큰 수 출력
print(nums[idx])


## 정답 풀이 
# 입력 
n = int(input())
a = list(map(int, input().split()))

# 자릿수 합 계산 함수
# 나머지/몫을 이용
def digit_sum(x):
    x_sum = 0
    while x>0:
        x_sum+=x%10   # 나머지
        x=x//10     # 몫
    return x_sum

max=-21470000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)


## 정답 풀이 2
# 입력 
n = int(input())
a = list(map(int, input().split()))

# 자릿수 합 계산 함수
# 문자열로 변환하여 계산
def digit_sum(x):
    x = str(x)
    x_sum = 0
    for i in str(x):
        x_sum+=int(i)
    return x_sum

max=-21470000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)
