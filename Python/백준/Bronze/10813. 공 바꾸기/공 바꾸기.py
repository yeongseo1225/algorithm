N, M = map(int,input().split())
#N 바구니 개수
#M 공을 바꿀 횟수
#처음부터 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있음
# 공을 바꿀 바구니 2개를 선택, 두 바구니에 들어있는 공을 교환
arr = []
for i in range(N):
    arr.append(i+1)
for _ in range(M):
    i,j = map(int,input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
print(*arr)   