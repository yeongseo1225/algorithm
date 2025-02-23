N = int(input())
my_list = list(map(int,input().split()))
v = int(input())
cnt = 0

for i in my_list:
    if(i == v):
        cnt = cnt + 1
print(cnt)