info = int(input())
stick = []
cnt = 0
bef = '' # 직전 x
for x in info:
    stick.append(x)
    if stick and x==')':
        if bef=='(': # () 인 경우
            cnt += len(stick)-2 # len(stick) 에서 laser 제외한 개수
            stick.pop() # laser 삭제
            stick.pop()
        else: # 막대 끝난 경우
            cnt += 1
            stick.pop() # 막대 삭제
            stick.pop()
    bef = x
cnt += len(stick) # 마지막 레이저 이후의 조각

print(cnt)
