# 정답 풀이

n = int(input())

meeting = []
for i in range(n):
    s, e = map(int, input().split()) # 시작 시간, 끝나는 시간
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0])) # 회의 끝나는 시간(x[1]) 기준으로 정렬
et = 0 # 회의 끝나는 시간
cnt = 0

for s, e in meeting: 
    if s >= et:  # 새로운 회의 시작시간이 이전 회의 끝나는 시간보다 같거나 늦음
        et = e
        cnt += 1
print(cnt)
