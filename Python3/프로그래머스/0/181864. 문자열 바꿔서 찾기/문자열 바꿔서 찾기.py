def solution(myString, pat):
    text = ""
    for i in myString:
        if i == "A":
            text += "B"
        elif i == "B":
            text += "A"
    if pat in text:
        answer = 1
    else:
        answer = 0
    return answer