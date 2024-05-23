a = list(map(int,input().split())) # map int를 안쓰면  str으로 정렬하게 되어 틀린다!
a.sort()
print(a[0], a[1], a[2])
