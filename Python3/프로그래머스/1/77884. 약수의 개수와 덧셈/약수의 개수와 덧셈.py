import math
def solution(left, right):
    answer = 0
    for num in range(left,right+1):
        if int(math.sqrt(num)) == math.sqrt(num): #제곱근이 정수이면 약수가 홀수개
            answer -= num
        else:
            answer += num
                
    return answer