# 입력 
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 투 포인터 적용 
res = 0
# 중간 인덱스 지정
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    # 행이 n//2보다 작으면 탐색 범위를 늘린다.
    if i<n//2:
        s-=1
        e+=1
    # 행이 n//2보다 크면 탐색 범위를 줄인다.
    else:
        s+=1
        e-=1
print(res)
