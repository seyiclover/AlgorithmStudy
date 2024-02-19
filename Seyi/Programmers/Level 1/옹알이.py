def solution(babbling):
    cnt = 0
    babble = ["aya", "ye", "woo", "ma"]
    for utter in babbling:
        for word in babble:
            if word * 2 not in utter:
                utter = utter.replace(word, ' ')
        if utter.strip() == '':
            cnt += 1

    return cnt
