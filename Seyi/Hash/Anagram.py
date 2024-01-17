# hash 1
a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x]=str1.get(x, 0)+1
for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")


# hash 2
# 개선된 코드
a=input()
b=input()
sH=dict()
# a문자열을 순회하면서 sH에 키값을 추가하고 키값이 있으면 1을 더한다.
for x in a:
    sH[x]=sH.get(x, 0)+1
# b문자열을 순회하면서 sH에 키값을 추가하고 키값이 있으면 1을 뺀다.
for x in b:
    sH[x]=sH.get(x, 0)-1

# a와 b의 문자열의 개수가 같으면 해당 문자열의 키값은 0이 된다.
for i in sH.keys():
    if sH[x]!=0:
        print("NO")
        break
else:
    print("YES")

# hash 3
# 리스트해쉬 적용 코드 
a=input()
b=input()
# 알파벳 대소문자는 총 52개
str1=[0]*52
str2=[0]*52

for x in a:
    # 대문자 알파벳 아스키코드 65~90 => 65를 빼면 0~25로 변환
    if x.isupper():
        str1[ord(x)-65]
    # 소문자 알파벳 아스키코드 97~122 => 71을 빼면 26~51로 변환
    else:
        str1[ord(x)-71]

for x in b:
    # 대문자 알파벳 아스키코드 65~90 => 65를 빼면 0~25로 변환
    if x.isupper():
        str2[ord(x)-65]
    # 소문자 알파벳 아스키코드 97~122 => 71을 빼면 26~51로 변환
    else:
        str2[ord(x)-71]

for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("Yes")
