def find_number(n, m):
    m.sort()
    lt=0
    rt=len(m)-1

    while lt<=rt:
        mid=(lt+rt)//2
        if m[mid]==n:
            return "yes"
        elif m[mid]<n:
            lt=mid+1
        else:
            rt=mid-1
    return "no"

n = int(input())        # 가게의 부품 개수 입력
n_list = list(map(int, input().split()))        # 가게의 부품 번호 입력 
m = int(input())        # 손님이 확인 요청한 부품 개수 입력 
m_list = list(map(int, input().split()))        # 손님이 확인 요청한 부품 번호 입력 

# 손님이 확인 요청한 부품 번호 하나씩 확인 
for x in m_list:
    print(find_number(x, n_list), end=' ')
