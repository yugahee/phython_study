# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):  
    numbers.sort()
    
    answer1 = numbers[0] * numbers[1]
    answer2 = numbers[len(numbers)-1] * numbers[len(numbers)-2]

    if answer1 > answer2:
        return answer1
    else:
        return answer2