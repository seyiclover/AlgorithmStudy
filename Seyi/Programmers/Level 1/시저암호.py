def solution(s, n):
   
    result = "" # 결과값
   
    # 문자열 s에서 알파벳 반복문 조회
    for alp in s:
       
        # 공백일 땐 result에 공백 추가하기
        if alp == " ":
            result += " "
       
        # chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수
        # ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수
       
        # alp가 소문자일 때
        elif alp.islower():
            result += chr((ord(alp)-ord('a') + n) % 26 + ord('a'))
       
        # alp가 대문자일 때
        elif alp.isupper():
            result += chr((ord(alp)-ord('A') + n) % 26 + ord('A'))
   
   
    return result
