arr = [input() for _ in range(5)] #입력받기
for j in range(15):
    for i in range(5):
        if j < len(arr[i]):
            print(arr[i][j],end="")
    
        