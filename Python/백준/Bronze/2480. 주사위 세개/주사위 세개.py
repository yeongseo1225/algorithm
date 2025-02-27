A, B, C = map(int,input().split())

#같은 눈이 3개 나오는 경우
if A == B == C:
    print(10000 + A * 1000)
#같은 눈이 2개만 나오는 경우    
elif A == B:
    print(1000+A*100)
elif A == C:
    print(1000+A*100)
elif B == C:
    print(1000+B*100)       
#모두 다른 눈이 나오는 경우 
elif A != B != C:
    max_value = max(A,B,C)
    print(max_value * 100)
        