#문자열 배열 strlist가 매개변수로 주어집니다. 
# strlist 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(strlist):
    answer = []
    
    for str in strlist:
        answer.append(len(str))
        
    return answer