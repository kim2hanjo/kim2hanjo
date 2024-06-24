# 프로그래머스 숫자 문자열과 영단어
def solution(s):
    eng_dict = { '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
                '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine' }
    
    for key, value in eng_dict.items():
        s = s.replace(value, key)
    
    return s

print(solution("one4seveneight"))

