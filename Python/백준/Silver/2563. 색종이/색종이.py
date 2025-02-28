N = int(input()) #색종이 수
#도화지 크기 100x100 가로 세로
#색종이 크기 10x10 가로 세로
#도화지 2차원 배열로 만들기
arr = []
for _ in range(100):
    arr.append([0]*100)
#색종이 붙이기
for i in range(N):
    X,Y = map(int,input().split()) #색종이 붙은 위치 
    for j in range(X,X+10):
        for k in range(Y,Y+10):
            arr[j][k] = 1
#색종이 붙은 공간 계산하기
area = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            area+=1
print(area)            