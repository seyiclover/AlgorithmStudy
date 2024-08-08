n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)     # 1번 인덱스가 리스트의 첫번째 수가 되도록 맞춤

# 해당 인덱스에서 만들 수 있는 가장 긴 증가수열의 길이를 저장할 리스트 초기화
dy = [0] * (n+1)
dy[1] = 1       # 첫번째 항의 증가수열 길이의 최대값은 1
# 부분증가수열의 최대 길이값
res = 0
for i in range(2, n+1):     # 현재 조회하는 항
    max = 0
    for j in range(i-1, 0, -1):     # i 항의 앞에 있는 항들을 비교
        if arr[j] < arr[i] and dy[j] > max:     # i 항의 수보다 j가 작아야하고 max보다 증가수열 값이 크다면 max를 갱신
            max = dy[j]
    dy[i] = max + 1
    if dy[i]>res:
        res=dy[i]

print(res)
