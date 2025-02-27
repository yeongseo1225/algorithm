chess = [1,1,2,2,2,8] #있어야 하는 개수
arr = list(map(int,input().split())) #가지고 있는 개수

for i in range(len(arr)):
    print(chess[i] - arr[i],end=" ")


        
        
        