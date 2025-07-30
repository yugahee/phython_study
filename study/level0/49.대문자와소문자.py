# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = ''
    
    for str in list(my_string):
        if str.isupper():
            answer += str.lower()
        else:
            answer += str.upper()
    
    return answer

# .swapcase()를 사용하면 바로 exchange 된다