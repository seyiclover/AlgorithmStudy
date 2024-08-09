sum_ = 0
cnt = 0
i = 0


def DFS(numbers, target, sum_, i):
    if i == len(numbers):
        if sum_==target:
            global cnt 
            cnt += 1
        return
    
    else:
        DFS(numbers, target, sum_+numbers[i], i+1) # +
        DFS(numbers, target, sum_-numbers[i], i+1) # -

def solution(numbers, target):
    DFS(numbers, target, sum_, i)
    return cnt
