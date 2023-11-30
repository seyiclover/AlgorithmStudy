# 입력
n, m = map(int, input().split())
answer = 0
# 한 줄씩 입력받아 최솟값 중에서 최댓값 찾기
for _ in range(n):
    arr = list(map(int, input().split()))
    min_value = min(arr)    # 현재 행에서 가장 작은 수 찾기
    answer = max(result, min_value)     # 가장 작은 수들 중에서 가장 큰 수 찾기
print(answer)
