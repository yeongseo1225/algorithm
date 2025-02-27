#윤년
#4의 배수 + 100의 배수X
#or
#4의 배수 + 400의 배수O
# 400년 -> 100의 배수 X -> 400의 배수 O -> 윤년
y = int(input()) #입력받기
if y % 4 == 0:
    if y % 100 != 0 or y % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)