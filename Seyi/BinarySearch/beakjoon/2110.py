# 입력
n, c = map(int, input().split())
house_list = [int(input()) for _ in range(n)]

# 정렬
house_list.sort()

# 이진 탐색을 위한 시작점과 끝점 설정
start = house_list[0]
end = house_list[-1]

answer = 0
while start <= end:
    mid = (start+end)//2
    # 공유기 설치
    cnt = 1
    # 첫번째 집에 공유기 설치
    last = house_list[0]
    for i in range(1, n):
        if house_list[i] >= last+mid:
            cnt += 1
            last = house_list[i]
    # 공유기의 수가 c보다 작으면 간격을 줄이고
    if cnt < c:
        end = mid - 1
    # 공유기의 수가 c보다 크거나 같으면 간격을 늘림
    else:
        answer = mid
        start = mid + 1
print(answer)
