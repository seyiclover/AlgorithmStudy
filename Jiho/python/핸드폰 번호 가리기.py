def solution(phone_number):
    l = len(phone_number)-4
    new = '*' * l + phone_number[-4:]   
    return new