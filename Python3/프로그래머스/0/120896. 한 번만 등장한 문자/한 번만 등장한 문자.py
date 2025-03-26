def solution(s):
    answer = []
    for char in s:
        if s.count(char) == 1:
            answer.append(char)
    return "".join(sorted(answer))