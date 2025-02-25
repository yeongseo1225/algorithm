#9*9
#배열 선언
arr = []
#입력 받기
for _ in range(9):
    row = list(map(int,input().split())) #행에 입력 받기 ex) [1,2,3]
    arr.append(row) #입력 받은 행 배열에 하나씩 추가하기
#최댓값 구하기  
#일단 제일 처음 나온 값을 최대값이라고 
max_value = arr[0][0]  
#행 그리고 행 내의 요소를 돌면서 요소가 현재의 최댓값보다 크면 
#최대값에 넣어주기.
for row in arr:
    for elem in row:
        if elem > max_value:
            max_value = elem
#행 길이만큼 돌기
for i in range(len(arr)): #행을 돌 때 사용하는 방법
    #최대값이 i행 안에 있다면
    if max_value in arr[i]:
        #위치값 지정하기
        index_value = (i+1,(arr[i].index(max_value))+1)
        #행의 위치, arr[i]에서 max_value의 위치    
print(max_value)
print(*index_value)
    