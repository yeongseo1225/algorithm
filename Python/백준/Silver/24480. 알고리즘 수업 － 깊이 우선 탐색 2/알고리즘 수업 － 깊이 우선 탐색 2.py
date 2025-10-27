import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1): #내림차순으로 인접노드 방문하기 위해 정렬 
    graph[i].sort(reverse=True)

c = 1
def DFS(v):
    global c
    visited[v] = c
    for i in graph[v]:
        if visited[i] == 0:
            c += 1
            DFS(i)
DFS(r)

for i in range(1, n+1):
    print(visited[i])
    