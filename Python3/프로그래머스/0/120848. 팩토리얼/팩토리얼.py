import math
def solution(n):
    answer = 0
    for i in range(1,12):
        if n < math.factorial(i):
            # 7 3 6
            #  4 24
            # 
            return i-1