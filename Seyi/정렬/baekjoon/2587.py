a = []
for _ in range(5):
    a.append(int(input()))

# a의 평균 
print(int(sum(a)/5))
# a의 중앙값
a.sort()
print(a[2])
