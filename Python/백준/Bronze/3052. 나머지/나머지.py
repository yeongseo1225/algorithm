left_list = [] #나머지 값을 받을 리스트
for i in range(10):
    num = int(input()) #숫자 입력받기
    left_list.append(num%42) #42의 나머지 바로 집어넣기

print(len(set(left_list))) #set 함수는 중복을 허용하지 않기 때문에 서로 다른 값만 남음


    
    
    