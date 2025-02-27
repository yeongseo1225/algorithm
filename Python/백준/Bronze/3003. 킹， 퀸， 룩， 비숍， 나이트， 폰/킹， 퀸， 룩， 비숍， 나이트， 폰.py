arr = [1,1,2,2,2,8] #있어야 하는 개수
arr1 = list(map(int,input().split())) #가지고 있는 개수

#피스 완성을 위한 개수
arr2 = []
for _ in range(len(arr1)):
    arr2.append(0)
    
for i in range(len(arr1)):
    if arr1[i] > arr[i]:
        arr2[i] = arr[i]-arr1[i]
    elif arr1[i] < arr[i]:
        arr2[i] = arr[i] - arr1[i] #있어야하는 개수 - 가지고 있는 개수
print(*arr2)        


        
        
        