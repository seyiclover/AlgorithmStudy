import sys
input = sys.stdin.readline

n, k = map(int,input().split())
S = input().rstrip()
eat_list = list(S)
cnt = 0

for i in range(len(eat_list)):
    if eat_list[i] == "P": #만약 사람이 나온다면
        for j in range(i-k, i+k+1): #사람에서 k만큼 왼쪽에서 k만큼 오른쪽을 살펴본다.
            if 0 <= j < n and eat_list[j] == "H": #만약 사람이 맨 처음에 나온다면 j가 -1이 될수도 있으므로 and 좌측조건 추가
                cnt += 1
                eat_list[j] = "0"
                break #두번째 for문에서 빠져나온다.

print(cnt)
