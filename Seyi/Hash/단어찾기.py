# 단어 개수 입력
n=int(input())
# 해쉬 형태로 단어 입력
p=dict()
# 노트에 있는 단어는 value 1
for i in range(n):
    word=input()
    p[word]=1
# 시에 쓰인 단어는 value 0
for i in range(n-1):
    word=input()
    p[word]=0
# val=1 이면 시에 쓰이지 않은 단어
for key, val in p.items():
    if val==1:
        print(key)
        break
