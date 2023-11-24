def solution(n, lost, reserve):
    # 여벌 체육복을 가진 학생 중 도난 당한 학생 제외
    reserve= set(reserve)-set(lost)
    lost=set(lost)
    # 여벌 체육복을 빌릴 수 있는 학생 추리기
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    # 전체 학생 중에서 체육복을 입을 수 없는 학생 제외 
    return n-len(lost)
