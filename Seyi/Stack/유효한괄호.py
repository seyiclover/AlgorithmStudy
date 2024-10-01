def isValid(s: str) -> bool:
    # 괄호의 짝을 저장할 딕셔너리
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in s:
        # 닫는 괄호일 경우
        if char in bracket_map:
            # 스택의 마지막 요소와 비교 (스택이 비어 있으면 # 으로 대체)
            top_element = stack.pop() if stack else '#'
            # 짝이 맞지 않으면 False 반환
            if bracket_map[char] != top_element:
                return False
        else:
            # 여는 괄호일 경우 스택에 추가
            stack.append(char)
    
    # 스택이 비어있으면 True, 비어있지 않으면 False
    return not stack
