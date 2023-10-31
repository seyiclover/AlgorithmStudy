def solution(n):
    # n을 2로 나눈 몫과 나머지 활용
  
    letter = '수박'
    answer = ''
    left = n % 2
    
    if left == 0:        # 몫만큼 '수박'을 반복
        answer = letter * (n // 2)
    else:           # 나머지가 1이면 '수' 추가 
        answer = letter * (n // 2) + letter[0] 
    return answer
