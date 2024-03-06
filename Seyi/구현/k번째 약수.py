## 내 풀이
# 입력 
n, k = map(int, input().split())

# 약수 판별 
res = []
for i in range(1, n+1):
    if n % i ==0:
        res.append(i)

# k번째 약수 출력 
if len(res) >= k:
    print(res[k-1])
else:
    print(-1)

## 정답 풀이 
# 입력 
n, k = map(int, input().split())
# 약수 판별 
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
# k번째 약수를 찾지 못하고 반복문이 종료되면 실행 => for break else 구문 
else:
    print(i)
