from collections import deque

# 필수과목 입력 
n = input()
# 수업 설계 개수
num = int(input())
# 설계된 수업 
lst = list(map(str, input().split()))
print(n, num, lst)
# 수업 설계 판단 함수 
def check_plan(n, num, plan):
    Q = deque(list(plan))
    tmp = []
    while Q:
        cur = Q.popleft()
        if cur in n and cur not in tmp:
            tmp.append(cur)
            if len(tmp)==len(n):
                if ''.join(tmp)==n:
                    print(tmp, 'YES')
                    break
                else:
                    print(tmp, 'NO')
                    break

for plan in lst:
    check_plan(n, num, plan)
