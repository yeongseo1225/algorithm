n = int(input())
score_list = list(map(int,input().split()))
m = max(score_list)

sum = 0
for i in range(n):
    score_list[i] = score_list[i]/m*100
    sum += score_list[i]

print(sum/n)