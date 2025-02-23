N = int(input()) #숫자의 갯수
S = input() #문자열로 입력 받기
sum = 0
for i in range(N):
    sum = sum + int(S[i]) #문자열 정수형으로 변환
print(sum)