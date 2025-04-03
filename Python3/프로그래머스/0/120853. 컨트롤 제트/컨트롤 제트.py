def solution(s):
    arr = []
    for i in s.split():
        if i != "Z":
            arr.append(int(i))
        else:
            arr.pop()
    return sum(arr)