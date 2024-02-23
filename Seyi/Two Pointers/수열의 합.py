n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt=0
lt=0
rt=1
# 수열의 합 저장
tot = nums[0]
while True:
    # 수열의 합이 m보다 작으면 rt를 키운다 
    if tot<m:
        if rt<n:
            tot+=nums[rt]
            rt+=1
        # rt 가 n이되면 반복문 종료
        else:
            break
    # 수열의 합이 m이되면 cnt를 키우고 lt를 증가시킨다
    elif tot==m:
        cnt+=1
        tot-=nums[lt]
        lt+=1
    # 수열의 합이 m보다 크면 lt를 증가시킨다
    else:
        tot-=nums[lt]
        lt+=1

print(cnt)
