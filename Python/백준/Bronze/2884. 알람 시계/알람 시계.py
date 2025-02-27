H,M = map(int,input().split())

#3가지 경우
#분이 45보다 클 때 
#분이 45보다 작을 때
#45보다 작은 경우에서 자정을 넘어갔을때
# 2 : 25


if M >= 45:
    print(H, M-45)
elif M < 45:
    if H >= 1:
        print(H-1, M+15)
    else:
        print(H+23, M+15)
    
    