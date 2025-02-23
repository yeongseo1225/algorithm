N, X = map(int,input().split())
A_list = list(map(int,input().split()))
result_list = []

for i in A_list:
    if i < X:
        result_list.append(i)
result = " ".join(map(str,result_list))
print(result)