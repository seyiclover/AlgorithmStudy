import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())

target = [3, 13, 23]


a_result = 60 * 60  # 시간 자리에 3 있는 경우
b_result = (((10*6*10) + (5*6*10) + (5*9*10) + (5*9*5)))

result = 0
for i in range(n+1):
    if i in target:
        result += a_result
    else:
        result += b_result

print(result)


'''
- 파이썬은 1초에 20,000,000번 정도의 연산을 수행하므로 이 문제는 완전 탐색이 적절
- 실행 시간도 완전 탐색이 빠름. 

N = int(input())

cnt=0

for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            time = str(hour)+str(minute)+str(second)
            if '3' in time:
                cnt+=1
                
print(cnt)
'''
