## 내 풀이 
# 입력 
m = int(input())
# k번째 수 출력 
for i in range(m):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums = nums[s-1:e]
    # 오름차순 정렬
    nums.sort()
    print(nums[k-1])

## 정답 풀이 
T = int(input())

# k번째 수 출력 
for i in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = a[s-1:e]
    a.sort()
    print("%d %d" %(T+1, a[k-1]))
