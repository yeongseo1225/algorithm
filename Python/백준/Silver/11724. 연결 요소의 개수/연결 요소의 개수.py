import sys
sys.setrecursionlimit(10000)
#DFS를 재귀로 짤 때, 깊이가 클 수 있으니 재귀 한계를 늘려주는 것
input = sys.stdin.readline
n, m = map(int, input().split()) #입력 받기
A = [[] for _ in range(n+1)] #빈 인접 리스트 만들기 
visited = [False] * (n+1) #방문 리스트에 전부 False 넣어놓기

def DFS(v): #DFS 함수
    visited[v] = True #방문하려는 노드 방문으로 수정
    for i in A[v]: #ex)A[1]의 인접 리스트 2,5 방문
        if not visited[i]:# 방문하지 않았으면
            DFS(i) #DFS

for _ in range(m): #인접 리스트 만들기
    s, e = map(int, input().split())
    A[s].append(e) # 1 2 면 1 2
    A[e].append(s) # 2 1 로 연결되어있음

count = 0 #DFS 실행 횟수

for i in range(1, n+1):
    if not visited[i]: #방문하지 않은 노드라면
        count += 1 #DFS 실행 횟수 +1
        DFS(i) #DFS 실행
        
            
print(count)