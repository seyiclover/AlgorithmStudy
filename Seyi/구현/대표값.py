# 입력
n = int(input())
scores = list(map(int, input().split()))
# scores = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]

# 평균 
m_scores = round(sum(scores) / n)

# 평균이 가장 가까운 수 출력 
lowest_abs = float('inf')
closest = []
for idx, score in enumerate(scores):
    diff = abs(m_scores - score)
    if idx == 0:
        lowest_abs = diff
        closest = [idx, score]
    else:
        if diff <= lowest_abs and score > closest[1]:
            lowest_abs = diff
            closest = [idx, score]
    
print(m_scores, closest[0]+1)

## 정답풀이 

n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)       #평균
lowest = 2147000000

for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<lowest:
        lowest = tmp  # 평균과의 차이값이 가장 작을 경우 저장
        score=x       # 차이값이 같을 경우 점수비교를 위해 점수 저장
        res=idx+1     # 정답이되는 학생번호
    elif tmp==lowest:
        if x>score:
            score=x
            res=idx+1

print(ave, res)
