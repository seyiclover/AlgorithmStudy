def solution(answers):

    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for answer in answers:

        cnt1 = 0
        for i in range(len(answers)):
            if st1[(i % 5)] == answers[i]:
                cnt1 += 1

        cnt2 = 0
        for i in range(len(answers)):
            if st2[(i % 8)] == answers[i]:
                cnt2 += 1

        cnt3 = 0
        for i in range(len(answers)):
            if st3[(i % 10)] == answers[i]:
                cnt3 += 1
        
        scores = sorted([cnt1, cnt2, cnt3])
        
        if cnt1 > cnt2 and cnt1 > cnt3:
            return [1]

        elif cnt2 > cnt1 and cnt2 > cnt3:
            return [2]
        
        elif cnt3 > cnt1 and cnt3 > cnt2:
            return [3]
        
        elif cnt1 == cnt2 == cnt3:
            return [1, 2, 3]
        
        elif cnt1 == cnt2:
            return [1, 2]
        
        elif cnt1 == cnt3:
            return [1, 3]
        
        elif cnt2 == cnt3:
            return [2, 3]
        

    return scores



# 깔끔한 풀이

'''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''