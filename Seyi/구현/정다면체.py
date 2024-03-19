## 내 풀이
# 입력 
n, m = map(int, input().split())
n_dice = [i for i in range(1, n+1)]
m_dice = [i for i in range(1, m+1)]

# 두 주사위의 합
res = []
for i in n_dice:
    for j in m_dice:
        res.append(i+j)

# 빈도수 계산
cnt = [0]*(n+m-1)
for i in res:
    cnt[i-2] += 1

# 최대 빈도수
max_cnt = max(cnt)
for idx, c in enumerate(cnt):
    if c == max_cnt:
        print(idx+2, end=' ')

## 정답 풀이 

n, m = map(int, input().split())

# 빈도 수 카운트(넉넉하게 0으로 초기화)
cnt=[0]*(n+m+3)
max_cnt=-2147000000

# 모든 경우의 수 탐색
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

for i in range(n+m+1):
    if cnt[i]>max_cnt:
        max_cnt=cnt[i]

for i in range(n+m+1):
    if cnt[i]==max_cnt:
        print(i, end=' ')   # 개행 제거
