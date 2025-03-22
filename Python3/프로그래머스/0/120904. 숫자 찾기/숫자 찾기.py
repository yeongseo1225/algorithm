def solution(num, k):
    num = str(num)
    k = str(k)
    try:
        answer = str(num).index(k) + 1
        return answer
    except:
        return -1
