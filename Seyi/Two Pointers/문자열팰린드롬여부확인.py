def is_palindrome_two_pointers(s: str) -> bool:
    # 문자열을 소문자로 변환하고, 공백 및 특수문자 제거
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # 좌우 포인터 설정
    left, right = 0, len(s) - 1
    
    # 포인터가 중앙에서 만나기 전까지 반복
    while left < right:
        # 왼쪽과 오른쪽 문자가 다르면 팰린드롬이 아님
        if s[left] != s[right]:
            return False
        # 포인터를 각각 중앙으로 한 칸씩 이동
        left += 1
        right -= 1
    
    # 모든 문자가 일치하면 팰린드롬임
    return True
