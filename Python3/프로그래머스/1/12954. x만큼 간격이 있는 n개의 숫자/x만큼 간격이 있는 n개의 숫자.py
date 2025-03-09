def solution(x, n):
    answer = []
    temp = x # 2
    for i in range(n):
        answer.append(x)
        x += temp
    return answer