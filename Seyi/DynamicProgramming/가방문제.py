# 냅색 알고리즘

n, m=map(int, input().split())
dy=[0]*(m+1)        # 가방의 무게 한도가 j일 때 보석의 최대 가치 저장 

for i in range(n):
    w, v=map(int, input().split())      # w: 보석의 무게, v: 보석의 가치 
    for j in range(w, m+1):
        dy[j]=max(dy[j], dy[j-w]+v)
        
print(dy[m])
