import string

S = input() #주어진 단어
#a~z까지 공백을 두고 출력.
#제시된 단어에 포함 되어 있는 경우에는 처음 등장하는 위치를, 
#포함되지 않는 경우에는 -1을 출력

a_list = list(string.ascii_lowercase) #a~z 소문자를 담은 리스트 생성
result_list = [] #결과 리스트
for i in a_list:
    result_list.append(S.find(i)) #i가 S에 포함되어 있으면 찾아서 그 위치를 저장
print(" ".join(map(str,result_list)))    
        
