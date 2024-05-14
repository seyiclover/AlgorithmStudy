n = int(input())

p = list(map(int, input().split()))
p.sort()    # 시간이 적게 걸리는 순서대로 인출하면 최소합 도출 가능

answer = 0
for i in range(n):      # 각 사람별 누적 대기시간의 합
    for j in range(i+1): 
        answer += p[j]

print(answer)
