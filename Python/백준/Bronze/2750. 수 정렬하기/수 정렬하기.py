N = int(input())

arr =[]
for i in range(N):
    num = int(input())
    arr.append(num)
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr [j]: #큰 값을 뒤로 보냄.
            arr[i], arr[j] = arr[j], arr[i]
print(*arr)            
            
    
     
    