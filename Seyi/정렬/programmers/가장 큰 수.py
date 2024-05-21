def solution(numbers):
    answer = ''
    # string 변환 
    numbers = list(map(str, numbers))
    # 3번씩 반복된 수가 가장 큰 순서대로 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    for i in numbers:
        answer += i
        
    return str(int(answer))
