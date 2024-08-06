def solution(s, n):
    
    upper = [chr(ch) for ch in range(ord('A'), ord('Z')+1)]
    lower = [chr(ch) for ch in range(ord('a'), ord('z')+1)]

    a = ''
    for char in s:
        if char in upper:
            new_index = upper.index(char) + n

            if new_index + upper.index(char) < len(upper):
                i = upper.index(char) + n

            else:
                i = new_index - len(upper)
                
            char = upper[i]

        elif char in lower:
            new_index = lower.index(char) + n

            if new_index + lower.index(char) < len(lower):
                i = lower.index(char)+n

            else:
                i = new_index - len(lower)
                
            char = lower[i]

        a += char

    return a


