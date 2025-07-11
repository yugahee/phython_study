# 정수가 담긴 리스트 num_list가 주어질 때,
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.


def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        
    answer.append(even)
    answer.append(odd)
    
    return answer
