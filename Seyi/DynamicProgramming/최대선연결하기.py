'''
선이 교차하지 않으려면 오른쪽 배열이 감소하지 않는 추세여야한다.
연결된 선의 길이가 최대가 되기 위해서는 최대 부분 증가수열을 찾아야한다. 
'''

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dy = [0] * (n+1)        # 왼쪽 번호 기준 연결할 수 있는 선의 길이 저장 
dy[1] = 1
res = 0                 # 겹치지 않게 최대로 그릴 수 있는 선의 개수

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)
