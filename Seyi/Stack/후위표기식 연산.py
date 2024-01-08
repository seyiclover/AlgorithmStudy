# 백준 1935

# 피연산자 수
n = int(input())
# 후위표기식 입력
s = input()
# 피연산자 리스트 생성
n_list = [int(input()) for i in range(n)]

stack = []

for x in s:
    # 알파벳을 숫자로 변환하여 stack에 넣는다.
    # 해당 알파벳을 아스키 코드로 바꾸어 'A'의 아스키코드 값인 65를 뺀 값을 인덱스로하는 num을 스택에 넣는다.
    if x.isalpha():
        stack.append(n_list[ord(x)-ord('A')])
    # 연산자일 경우 스택에서 숫자 2개를 꺼내 연산한다.
    elif x=='+':
        stack.append(stack.pop(-2)+stack.pop(-1))
    elif x=='-':
        stack.append(stack.pop(-2)-stack.pop(-1))
    elif x=='*':
        stack.append(stack.pop(-2)*stack.pop(-1))
    elif x=='/':
        stack.append(stack.pop(-2)/stack.pop(-1))

print('%.2f' %stack.pop())
