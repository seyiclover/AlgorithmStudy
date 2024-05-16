a = input()
b = a.split('-')

answer = 0

# 처음에 -로 시작할 경우의 수가 있어서 따로 작업 
x = sum(map(int, (b[0].split('+'))))

if a[0] == '-':
    answer -= x
else:
    answer += x

# 첫번째 숫자는 처리 했기 때문에 인덱스 1부터 시작
for i in b[1:]: 
    i = sum(map(int, (i.split('+'))))
    answer -= i

print(answer)
