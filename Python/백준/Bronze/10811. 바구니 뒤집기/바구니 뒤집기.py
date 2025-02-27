N,M = map(int,input().split())

#M번의 바구니의 순서를 역순으로 만들려고 한다...?
# 1 4 
# 4 3 2 1 5
arr = []
for i in range(N):
    arr.append(i+1)
for _ in range(M):
    i,j = map(int,input().split())
    while i < j: 
        arr[i-1], arr[j-1] = arr[j-1], arr[i-1] #두 값 교환
        i += 1
        j -= 1
        
print(*arr)        
    