import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = list(map(int,input().split()))
S = [0] * (N+1)

for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]

for _ in range(M):
    a,b = map(int,input().split())
    print(S[b]-S[a-1])