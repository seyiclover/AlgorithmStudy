import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for i in range(N):
    name, state = map(str, input().split())
    dic[name] = state

dic = sorted(dic.items(), reverse=True)

for key, value in dic:
    if value == 'enter':
        print(key)
