from itertools import combinations
def solution(numbers):
    combi = list(combinations(numbers,2))
    answer = []
    for i in combi:
        answer.append(i[0]*i[1])
    return max(answer)