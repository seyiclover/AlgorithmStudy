# 변수 입력
n, m, k=map(int, input().split())
nums=list(map(int, input().split()))
total=0
# nums 내림차순정렬 
nums.sort(reverse=True)
# 가장 큰 수를 k번 더하고 두번째로 큰 수를 1번 더해서 누적 m번째까지 더하는 것을 반복
while m>0:
    # k번 가장 큰 수를 더하고 두번째로 큰 수를 한번 더한다
    for i in range(k):
				# m이 0이 되면 반복문 중단
				if m==0: 
					break
        total+=nums[0]
        m-=1
    total+=nums[1]
    m-=1
print(total)
