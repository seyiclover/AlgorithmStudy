def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        answer.append(arr[i])
        if i > 0 and arr[i-1] == arr[i]:
            answer.pop()
            
    return answer
