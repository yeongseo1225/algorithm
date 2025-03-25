def solution(emergency):
    answer = []
    arr = sorted(emergency,reverse = True)
    for i in emergency:
        answer.append(arr.index(i)+1)
    
    return answer