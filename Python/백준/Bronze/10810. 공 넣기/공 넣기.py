N, M = map(int, input().split())
#N개의 바구니가 있음.
#M번의 공을 넣을 거임.
#ex) 1 2 3 은 1번 바구니부터 2번 바구니까지 3번의 공을 넣겠다.
# 바구니에 이미 공이 있는 경우 공을 빼고 새로 넣는다
# M 번의 공을 넣은 이후 각 바구니에 어떤 공이 들어있는지를 구하시오.
arr =[]
#바구니 전부 비어있게 초기화.
for _ in range(N):
    arr.append(0) 
for _ in range(M):
    i, j, k = map(int,input().split())
    # i ~ j -> k번의 공을 넣음
    # 
    for n in range(i-1,j): #1 4/ 1 3 / 0 3 1 -> 0, 
        arr[n] = k
print(*arr)        
    

