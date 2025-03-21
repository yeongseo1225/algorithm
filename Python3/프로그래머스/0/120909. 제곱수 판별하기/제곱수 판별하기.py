import math
def solution(n):
    answer = 0
    root = math.sqrt(n)
    if root.is_integer():
        answer = 1
    else:
        answer = 2
    return answer