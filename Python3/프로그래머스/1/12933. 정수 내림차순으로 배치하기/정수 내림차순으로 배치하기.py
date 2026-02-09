def solution(n):
    arr = list(map(int,str(n)))
    arr.sort(reverse=True)
    answer = int("".join(map(str,arr)))
    return answer