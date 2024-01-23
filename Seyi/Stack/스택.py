import sys

# 명령어 개수
# n = int(sys.stdin.readline())
n = int(input())
stack = []
# n개의 명령어 입력 
for i in range(n):
    # 명령어 입력
    # cmd = sys.stdin.readline()
    # 오른쪽 공백제거
    cmd = input().rstrip()
    # 명령어가 push인 경우
    if cmd[:4]=='push':
        stack.append(int(cmd[5:]))

    elif cmd=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif cmd=='size':
        print(len(stack))

    elif cmd=='empty':
        print(1 if len(stack)==0 else 0)

    elif cmd=='top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
