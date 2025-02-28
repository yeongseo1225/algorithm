N,K = map(int,input().split())
#N의 약수들 중 K번째로 작은 수를 출력.
arr =[]
for i in range(1,N+1):
    if N % i == 0:
        arr.append(i)
if len(arr) >= K:
    print(arr[K-1])
else: 
    print(0)
    