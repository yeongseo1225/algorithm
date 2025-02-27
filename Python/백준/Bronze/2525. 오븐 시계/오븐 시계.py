A, B = map(int,input().split()) #현재 시, 현재 분
C = int(input()) #요리하는데 필요한 시간

#더하기만 해도 될때
#분이 60분을 초과할때
#다음 날로 넘어갈때

if B+C >= 60:
    addH = (B+C)//60
    minitue = (B+C)%60
    if A+addH > 23:
        print(A+addH - 24, minitue)
    else:
        print(A+addH, minitue)
else:
    print(A, B+C) 
   