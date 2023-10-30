def solution(s):
    answer = ''
		# 공백 기준으로 단어 분리
    for word in s.split():
				# 단어 내 알파벳 인덱싱
        for idx, alp in enumerate(word):
						# 짝수일 때 대문자로 변환
            if idx % 2 == 0:
                answer += alp.upper()
						# 홀수일 때 소문자로 변환
            else:
                answer += alp.lower()
				# 단어가 조회될 때마다 공백 추가
        answer += ' '
		# 마지막 공백 제거하고 출력
    return answer[:-1]
