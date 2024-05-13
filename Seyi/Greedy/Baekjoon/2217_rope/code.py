n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)

b = []      # n번째 무게추의 무게 x n
for i in range(1, n+1):
    b.append(a[i-1]*i)

print(max(b))       # 최댓값 출력
