def solution(number):
    answer = 0
    comb_list = []
    # 원소 3개로 이루어진 정수 조합의 개수 => nCr 재귀함수 사용
    def comb(n, ans):
        if n == len(number):
            if len(ans) == 3:
                temp = [i for i in ans]
                comb_list.append(temp)
            return
        ans.append(number[n])
        comb(n+1, ans)
        ans.pop()
        comb(n+1, ans)
    
    # 재귀함수 호출
    comb(0, [])
    
    # 정수 번호 쌍의 합이 0인 경우의 수
    for i in comb_list:
        if sum(i) == 0:
            answer += 1
            
    return answer
