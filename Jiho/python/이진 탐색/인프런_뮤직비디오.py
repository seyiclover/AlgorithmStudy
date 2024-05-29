# 값(dvd 길이)의 범위: 1 ~ sum(곡들)

def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:  # 현재까지 저장된 용량 > capacity
            cnt += 1 # 새로운 dvd가 필요함
            sum = x
        else: # 같은 dvd에 계속 저장가능
            sum += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music)   # 가장 큰 노래 길이
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) <= m:   # mid >= maxx: dvd의 용량은 가장 큰 노래 길이보다 무조건 커야함
        res = mid
        rt = mid - 1
    else: # 용량 너무 작음
        lt = mid + 1

print(res) 
