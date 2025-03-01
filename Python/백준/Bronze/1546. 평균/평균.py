N = int(input()) #시험 본 과목의 개수
score = list(map(int,input().split())) #각 과목의 성적
M = max(score)
sum = 0
for i in score:
    sum += i/M*100
print(sum/N)    
 