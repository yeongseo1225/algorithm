N, M = map(int,input().split())
# N* M 크기의 두 행렬. N은 행 M은 열
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 
#N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

arrA = []
for _ in range(N):
    row = list(map(int,input().split())) 
    #공백을 기점으로 나눠서 리스트로 만듬 [1,2,3]
    arrA.append(row) 
arrB = []
for _ in range(N):
    row = list(map(int,input().split()))
    arrB.append(row) 
arrC = []
for i in range(N):
    arrC.append([0] * M)
    
#행렬 더하기        
for i in range(N):
    for j in range(M):
        arrC[i][j] = arrA[i][j] + arrB[i][j]
#출력
for i in range(N):
    for j in range(M):
        print(arrC[i][j],end=" ")
    print()
      
