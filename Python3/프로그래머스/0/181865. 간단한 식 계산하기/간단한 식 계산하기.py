def solution(binomial):
    answer = 0
    a,b,c = map(str,binomial.split())
    print(a)
    print(b)
    print(c)
    a = int(a)
    c = int(c)
    if b == "+":
        answer = a+c
    elif b == "-":
        answer = a-c
    elif b == "*":
        answer = a*c
            
    return answer