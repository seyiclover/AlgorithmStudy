import sys

# 빠른 입력을 위해 sys.stdin.readline() 사용
n = int(sys.stdin.readline().strip())

# 각 줄을 읽고 리스트에 저장
a = [sys.stdin.readline().strip() for _ in range(n)]

# 중복 제거
a = list(set(a))

# 길이순 정렬 후 알파벳순 정렬
a.sort(key=lambda x: (len(x), x))

# 결과 출력
for x in a:
    print(x)
