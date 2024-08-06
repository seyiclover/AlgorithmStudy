# DP
# 점화식

n = int(input())
dy = [0]*(n+1) # 1차원 배열(리스트)

dy[1] = 1 # 길이 1의 선을 자르는 방법은 1가지
dy[2] = 2 # 길이 2의 선을 자르는 방법은 2가지

for i in range(3, n+1): # 길이 3부터 dynamic 으로 구함
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n]) # n번째 출력
