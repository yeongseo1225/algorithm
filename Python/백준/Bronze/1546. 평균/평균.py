N = int(input()) #시험 본 과목 갯수
scr_list = list(map(int,input().split())) #과목 당 점수 
max_value = max(scr_list) #최고점
sum = 0
for i in range(N):
    scr_list[i] = scr_list[i]/max_value*100 # 점수/최댓값*100
    sum = sum + scr_list[i]
fake_avg = sum/N
print(fake_avg)