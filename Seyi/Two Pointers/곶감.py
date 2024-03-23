## 정답풀이 
# n, 격자 입력 
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 회전 명령 입력 & 처리
m = int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if t==0:    # 왼쪽회전
        for _ in range(k):
           a[h-1].append(a[h-1].pop(0))  # 0번 인덱스 값을 꺼낸 후 리스트 마지막에 append
    else:
        for _ in range(k):
           a[h-1].insert(0, a[h-1].pop())  # 마지막 인덱스 값을 꺼낸 후 리스트 맨 앞에 insert


# 모래 시계 탐색 
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:  
        s+=1s
        e-=1
    else:
        s-=1
        e+=1
print(res)
