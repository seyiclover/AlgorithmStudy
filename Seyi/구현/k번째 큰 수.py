## 정답 풀이 

# 입력 
n, k = map(int, input().split())
nums = list(map(int, input().split()))

res = set()     # 중복 제거 자료형
# 2중 for문으로 3개 카드 조합 생성 
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
            
# set 자료형은 sort() 기능이 없기 때문에 리스트로 변경 
res=list(res)
# 내림차순 정렬
res.sort(reverse=True)  
print(res[k-1])
