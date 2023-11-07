def solution(s):
  answer = ""
  cnt = 1
  s = s+ " "
  n = len(s)

  for i in range(n-1):  # s에 빈 문자를 추가했기 때문에 원본 s의 길이만큼 탐색 
    if s[i] == s[i+1]:
      cnt += 1
    else:
      answer += s[i]
      if cnt>1:
        answer += str(cnt)
      cnt=1

  return answer
