def solution(myString, pat):
    text = myString.replace("A","C").replace("B","A").replace("C","B")
    if pat in text:
        answer = 1
    else:
        answer = 0
    return answer