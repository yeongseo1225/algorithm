import sys

input = sys.stdin.readline
N, M = map(int,input().split())
#N : 수의 개수
#M : 합을 구해야하는 횟수
A = list(map(int,input().split()))
S = [0] #1<=i<=j<=N 이라서... 
sum = 0
for i in A:
    sum += i
    S.append(sum)
for _ in range(M):
    i,j = map(int,input().split())
    print(S[j]-S[i-1]) 
    
    

    