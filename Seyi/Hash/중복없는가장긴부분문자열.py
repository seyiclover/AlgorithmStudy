def length_of_longest_substring(s: str) -> int:
    # 문자의 인덱스를 저장할 딕셔너리
    char_map = {}
    # 부분 문자열의 시작 인덱스
    start = 0
    # 가장 긴 부분 문자열의 길이
    max_length = 0
    
    # 문자열의 각 문자를 순회
    for i, char in enumerate(s):
        # 문자가 이미 해시테이블에 있고, 그 인덱스가 시작점보다 클 때
        if char in char_map and char_map[char] >= start:
            # 부분 문자열의 시작 인덱스를 업데이트
            start = char_map[char] + 1
            
        # 현재 문자의 인덱스를 해시테이블에 저장
        char_map[char] = i
        # 현재 부분 문자열의 길이를 계산하고 최대 길이 업데이트
        max_length = max(max_length, i - start + 1)
    
    return max_length
